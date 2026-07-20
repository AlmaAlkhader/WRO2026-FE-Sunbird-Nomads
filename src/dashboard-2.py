#!/usr/bin/env python3
"""Sunbird robot dashboard and timed autonomous drive controller."""

import copy
import json
import signal
import statistics
import threading
import time
from collections import deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import parse_qs, urlparse

import adafruit_vl53l0x
import board
import RPi.GPIO as GPIO


# BCM GPIO numbering (physical pin numbers are in the comments).
LEFT_TRIG = 5       # physical pin 29
LEFT_ECHO = 6       # physical pin 31
RIGHT_TRIG = 20     # physical pin 38
RIGHT_ECHO = 21     # physical pin 40
SERVO_PIN = 12      # physical pin 32
MOTOR_EN = 13       # physical pin 33
MOTOR_IN1 = 23      # physical pin 16
MOTOR_IN2 = 24      # physical pin 18

# Steering calibration. Swap LEFT_ANGLE and RIGHT_ANGLE if steering is reversed.
SERVO_MIN_ANGLE = 30
SERVO_MAX_ANGLE = 150
CENTER_ANGLE = 106
LEFT_ANGLE = 81
RIGHT_ANGLE = 131

# Sensor and autonomous-control tuning.
ULTRA_MAX_CM = 400.0
AUTO_DIFF_CM = 35.0
AUTO_RATIO = 1.8
DECISION_CONFIRMATIONS = 3
MIN_SECTION_TIME_S = 1.5
SERVO_SETTLE_S = 0.45
WATCHDOG_S = 3.0

# PWM calibration.
SERVO_MIN_DUTY = 2.5
SERVO_MAX_DUTY = 12.5
MOTOR_PWM_HZ = 1000

HTML_PATH = "/home/sunbird/dashboard.html"


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEFT_TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(RIGHT_TRIG, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(LEFT_ECHO, GPIO.IN)
GPIO.setup(RIGHT_ECHO, GPIO.IN)
GPIO.setup(SERVO_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_EN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_IN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(MOTOR_IN2, GPIO.OUT, initial=GPIO.LOW)

servo_pwm = GPIO.PWM(SERVO_PIN, 50)
motor_pwm = GPIO.PWM(MOTOR_EN, MOTOR_PWM_HZ)
servo_pwm.start(0)
motor_pwm.start(0)

state_lock = threading.RLock()
servo_lock = threading.Lock()
motor_lock = threading.Lock()
state = {
    "tof_mm": None,
    "left_cm": None,
    "right_cm": None,
    "sensor_time": 0.0,
    "sensor_seq": 0,
    "angle": CENTER_ANGLE,
    "steering_direction": "center",
    "steering_reason": "Robot stopped",
    "running": False,
    "run_requested": False,
    "drive_state": "stopped",
    "motor_pwm": 0,
    "forward_speed": 55,
    "turn_speed": 45,
    "turn_duration": 1.0,
    "max_speed_cm_s": 50.0,
    "estimated_speed_cm_s": 0.0,
    "section_number": 0,
    "section_distance_cm": 0.0,
    "section_time_s": 0.0,
    "sections": [],
    "status_message": "Press Start Robot when the area is safe",
    "last_heartbeat": time.monotonic(),
}


def clamp(value, low, high):
    return max(low, min(high, value))


def angle_to_duty(angle):
    span = SERVO_MAX_ANGLE - SERVO_MIN_ANGLE
    position = (angle - SERVO_MIN_ANGLE) / span
    return SERVO_MIN_DUTY + position * (SERVO_MAX_DUTY - SERVO_MIN_DUTY)


def set_servo_angle(angle):
    """Set the commanded angle; a three-wire servo has no position feedback."""
    angle = int(round(clamp(float(angle), SERVO_MIN_ANGLE, SERVO_MAX_ANGLE)))
    with servo_lock:
        servo_pwm.ChangeDutyCycle(angle_to_duty(angle))
    with state_lock:
        state["angle"] = angle
    return angle


def motor_forward(duty):
    duty = round(clamp(float(duty), 0.0, 100.0), 1)
    with motor_lock:
        GPIO.output(MOTOR_IN1, GPIO.HIGH)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
        motor_pwm.ChangeDutyCycle(duty)
    with state_lock:
        state["motor_pwm"] = duty


def motor_stop():
    with motor_lock:
        motor_pwm.ChangeDutyCycle(0)
        GPIO.output(MOTOR_IN1, GPIO.LOW)
        GPIO.output(MOTOR_IN2, GPIO.LOW)
    with state_lock:
        state["motor_pwm"] = 0
        state["estimated_speed_cm_s"] = 0.0


def estimated_speed(pwm_percent, max_speed_cm_s):
    """Open-loop estimate only; actual speed requires a wheel encoder."""
    return max_speed_cm_s * clamp(pwm_percent, 0.0, 100.0) / 100.0


motor_stop()
set_servo_angle(CENTER_ANGLE)


def init_tof():
    try:
        i2c = board.I2C()
        sensor = adafruit_vl53l0x.VL53L0X(i2c)
        print("ToF sensor initialized at 0x29")
        return sensor
    except Exception as exc:
        print(f"ToF initialization failed: {exc}")
        return None


tof_sensor = init_tof()


def read_ultrasonic(trigger_pin, echo_pin, timeout=0.03):
    """Return centimetres, or None for no echo/stuck echo/out-of-range."""
    if GPIO.input(echo_pin):
        return None

    GPIO.output(trigger_pin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trigger_pin, GPIO.HIGH)
    time.sleep(0.000010)
    GPIO.output(trigger_pin, GPIO.LOW)

    deadline = time.monotonic() + timeout
    while not GPIO.input(echo_pin):
        if time.monotonic() >= deadline:
            return None

    pulse_start = time.monotonic()
    deadline = pulse_start + timeout
    while GPIO.input(echo_pin):
        if time.monotonic() >= deadline:
            return None

    distance_cm = (time.monotonic() - pulse_start) * 17150.0
    if not 2.0 <= distance_cm <= ULTRA_MAX_CM:
        return None
    return round(distance_cm, 1)


def filtered_value(samples, newest):
    if newest is not None:
        samples.append(newest)
    elif samples:
        samples.popleft()
    return round(statistics.median(samples), 1) if samples else None


def choose_turn_direction(left_cm, right_cm):
    """Return a turn only when one side is substantially more open."""
    if left_cm is None and right_cm is None:
        return "center", "No echo from both ultrasonic sensors"
    if left_cm is None:
        return "left", "Left has no echo (treated as open space)"
    if right_cm is None:
        return "right", "Right has no echo (treated as open space)"

    difference = abs(left_cm - right_cm)
    smaller = max(min(left_cm, right_cm), 1.0)
    ratio = max(left_cm, right_cm) / smaller
    if difference >= AUTO_DIFF_CM or (difference >= 20.0 and ratio >= AUTO_RATIO):
        if left_cm > right_cm:
            return "left", f"Left is clearer by {difference:.0f} cm"
        return "right", f"Right is clearer by {difference:.0f} cm"
    return "center", "Side distances are similar"


def direction_angle(direction):
    return {"left": LEFT_ANGLE, "right": RIGHT_ANGLE, "center": CENTER_ANGLE}[direction]


def sensor_loop():
    left_samples = deque(maxlen=3)
    right_samples = deque(maxlen=3)

    while True:
        try:
            tof_mm = int(tof_sensor.range) if tof_sensor is not None else None
        except Exception:
            tof_mm = None

        left_raw = read_ultrasonic(LEFT_TRIG, LEFT_ECHO)
        time.sleep(0.06)
        right_raw = read_ultrasonic(RIGHT_TRIG, RIGHT_ECHO)
        time.sleep(0.06)

        with state_lock:
            state["tof_mm"] = tof_mm
            state["left_cm"] = filtered_value(left_samples, left_raw)
            state["right_cm"] = filtered_value(right_samples, right_raw)
            state["sensor_time"] = time.time()
            state["sensor_seq"] += 1


def append_section(section_number, distance, moving_time, pwm_integral, turn):
    if section_number <= 0 or moving_time <= 0:
        return
    average_pwm = pwm_integral / moving_time
    average_speed_cm_s = distance / moving_time
    entry = {
        "section": section_number,
        "distance_cm": round(distance, 1),
        "moving_time_s": round(moving_time, 2),
        "average_pwm": round(average_pwm, 1),
        "average_speed_cm_s": round(average_speed_cm_s, 1),
        "ended_by": turn,
    }
    with state_lock:
        state["sections"].append(entry)
        state["sections"] = state["sections"][-30:]


def stop_request(message, emergency=False):
    with state_lock:
        state["run_requested"] = False
        state["running"] = False
        state["drive_state"] = "emergency stopped" if emergency else "stopped"
        state["status_message"] = message
    motor_stop()


def robot_loop():
    phase = "stopped"
    deadline = 0.0
    section_number = 0
    section_distance = 0.0
    section_moving_time = 0.0
    section_pwm_integral = 0.0
    pending_direction = "center"
    pending_count = 0
    last_sensor_seq = -1
    turn_direction = "center"
    section_open = False
    last_time = time.monotonic()

    def begin_section():
        nonlocal section_number, section_distance, section_moving_time
        nonlocal section_pwm_integral, pending_direction, pending_count, section_open
        section_number += 1
        section_open = True
        section_distance = 0.0
        section_moving_time = 0.0
        section_pwm_integral = 0.0
        pending_direction = "center"
        pending_count = 0
        with state_lock:
            state["section_number"] = section_number
            state["section_distance_cm"] = 0.0
            state["section_time_s"] = 0.0

    def finish_section(ended_by):
        nonlocal section_open
        if not section_open:
            return
        append_section(
            section_number,
            section_distance,
            section_moving_time,
            section_pwm_integral,
            ended_by,
        )
        section_open = False

    while True:
        now = time.monotonic()
        dt = min(now - last_time, 0.2)
        last_time = now

        with state_lock:
            requested = state["run_requested"]
            heartbeat_age = now - state["last_heartbeat"]
            forward_pwm = float(state["forward_speed"])
            turn_pwm = float(state["turn_speed"])
            turn_duration = float(state["turn_duration"])
            max_speed = float(state["max_speed_cm_s"])
            left_cm = state["left_cm"]
            right_cm = state["right_cm"]
            sensor_seq = state["sensor_seq"]

        if requested and heartbeat_age > WATCHDOG_S:
            finish_section("dashboard connection lost")
            stop_request("Safety stop: dashboard heartbeat lost", emergency=True)
            phase = "stopped"
            set_servo_angle(CENTER_ANGLE)
            time.sleep(0.02)
            continue

        if not requested:
            if phase != "stopped":
                finish_section("stopped by user")
                motor_stop()
                set_servo_angle(CENTER_ANGLE)
            phase = "stopped"
            with state_lock:
                if state["section_number"] == 0 and not state["sections"]:
                    section_number = 0
                state["running"] = False
                if state["drive_state"] != "emergency stopped":
                    state["drive_state"] = "stopped"
                state["steering_direction"] = "center"
            time.sleep(0.02)
            continue

        if phase == "stopped":
            set_servo_angle(CENTER_ANGLE)
            begin_section()
            motor_forward(forward_pwm)
            phase = "forward"
            with state_lock:
                state["running"] = True
                state["drive_state"] = "forward"
                state["steering_direction"] = "center"
                state["steering_reason"] = "Monitoring for the next turn"
                state["status_message"] = "Driving section"

        elif phase == "forward":
            speed_cm_s = estimated_speed(forward_pwm, max_speed)
            section_distance += speed_cm_s * dt
            section_moving_time += dt
            section_pwm_integral += forward_pwm * dt
            motor_forward(forward_pwm)
            with state_lock:
                state["estimated_speed_cm_s"] = round(speed_cm_s, 1)
                state["section_distance_cm"] = round(section_distance, 1)
                state["section_time_s"] = round(section_moving_time, 2)

            if sensor_seq != last_sensor_seq:
                last_sensor_seq = sensor_seq
                candidate, reason = choose_turn_direction(left_cm, right_cm)
                if candidate == pending_direction:
                    pending_count += 1
                else:
                    pending_direction = candidate
                    pending_count = 1

                with state_lock:
                    state["steering_reason"] = reason

                if (
                    section_moving_time >= MIN_SECTION_TIME_S
                    and candidate in ("left", "right")
                    and pending_count >= DECISION_CONFIRMATIONS
                ):
                    turn_direction = candidate
                    finish_section(turn_direction)
                    motor_stop()
                    set_servo_angle(direction_angle(turn_direction))
                    phase = "turn_steer"
                    deadline = now + SERVO_SETTLE_S
                    with state_lock:
                        state["drive_state"] = "positioning steering"
                        state["steering_direction"] = turn_direction
                        state["status_message"] = f"Motor stopped; steering {turn_direction}"

        elif phase == "turn_steer" and now >= deadline:
            motor_forward(turn_pwm)
            phase = "turn_drive"
            deadline = now + turn_duration
            with state_lock:
                state["drive_state"] = f"turning {turn_direction}"
                state["estimated_speed_cm_s"] = round(estimated_speed(turn_pwm, max_speed), 1)
                state["status_message"] = f"Timed {turn_direction} turn"

        elif phase == "turn_drive":
            motor_forward(turn_pwm)
            with state_lock:
                state["estimated_speed_cm_s"] = round(estimated_speed(turn_pwm, max_speed), 1)
            if now >= deadline:
                motor_stop()
                set_servo_angle(CENTER_ANGLE)
                phase = "turn_recenter"
                deadline = now + SERVO_SETTLE_S
                with state_lock:
                    state["drive_state"] = "recentering steering"
                    state["steering_direction"] = "center"
                    state["status_message"] = "Motor stopped; steering centered"

        elif phase == "turn_recenter" and now >= deadline:
            begin_section()
            motor_forward(forward_pwm)
            phase = "forward"
            with state_lock:
                state["drive_state"] = "forward"
                state["steering_reason"] = "Monitoring for the next turn"
                state["status_message"] = "Driving new section"

        time.sleep(0.02)


def snapshot_state():
    with state_lock:
        result = copy.deepcopy(state)
    result.pop("run_requested", None)
    result.pop("last_heartbeat", None)
    return result


def set_setting(name, value):
    limits = {
        "forward_speed": (0.0, 100.0),
        "turn_speed": (0.0, 100.0),
        "turn_duration": (0.2, 5.0),
        "max_speed_cm_s": (1.0, 300.0),
    }
    if name not in limits:
        raise ValueError(f"Unknown setting: {name}")
    low, high = limits[name]
    value = round(clamp(float(value), low, high), 2)
    with state_lock:
        state[name] = value


def handle_action(action):
    now = time.monotonic()
    if action == "heartbeat":
        with state_lock:
            state["last_heartbeat"] = now
    elif action == "start":
        with state_lock:
            state["last_heartbeat"] = now
            state["run_requested"] = True
            state["drive_state"] = "starting"
            state["status_message"] = "Start requested"
    elif action == "stop":
        stop_request("Stopped from dashboard")
    elif action == "emergency":
        stop_request("Emergency stop pressed", emergency=True)
    elif action == "reset_history":
        with state_lock:
            if state["running"]:
                raise ValueError("Stop the robot before clearing section history")
            state["sections"] = []
            state["section_number"] = 0
            state["section_distance_cm"] = 0.0
            state["section_time_s"] = 0.0
    else:
        raise ValueError(f"Unknown action: {action}")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *_args):
        pass

    def send_json(self, payload, status=200):
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/":
            try:
                with open(HTML_PATH, "rb") as html_file:
                    body = html_file.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Cache-Control", "no-store")
                self.end_headers()
                self.wfile.write(body)
            except OSError as exc:
                self.send_json({"error": str(exc)}, 500)
        elif parsed.path == "/data":
            self.send_json(snapshot_state())
        elif parsed.path == "/control":
            query = parse_qs(parsed.query)
            try:
                if "action" in query:
                    handle_action(query["action"][0])
                for setting in ("forward_speed", "turn_speed", "turn_duration", "max_speed_cm_s"):
                    if setting in query:
                        set_setting(setting, query[setting][0])
                if "angle" in query:
                    with state_lock:
                        if state["running"] or state["run_requested"]:
                            raise ValueError("Stop the robot before moving the steering manually")
                    set_servo_angle(float(query["angle"][0]))
                    with state_lock:
                        state["steering_direction"] = "manual"
                        state["steering_reason"] = "Angle selected from dashboard"
                self.send_json(snapshot_state())
            except (ValueError, TypeError) as exc:
                self.send_json({"error": str(exc)}, 400)
        else:
            self.send_json({"error": "Not found"}, 404)


def shutdown_hardware():
    try:
        stop_request("Dashboard shutting down")
        set_servo_angle(CENTER_ANGLE)
        time.sleep(0.25)
        servo_pwm.stop()
        motor_pwm.stop()
    finally:
        GPIO.cleanup()


def signal_shutdown(_signum, _frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGTERM, signal_shutdown)
signal.signal(signal.SIGINT, signal_shutdown)
threading.Thread(target=sensor_loop, daemon=True).start()
threading.Thread(target=robot_loop, daemon=True).start()

print("Dashboard at http://raspberrypi.local:8080")
try:
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
except KeyboardInterrupt:
    pass
finally:
    shutdown_hardware()
