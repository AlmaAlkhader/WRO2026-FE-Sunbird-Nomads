# Source Code

This code was used for testing and calibration of the Open Challenge (Task 1) — sensor readings, servo angles, turn timing, and speed settings were tuned through the live dashboard it exposes. **This is not the final code.** The final version will be added separately.


<img src="docs/dashboard-screenshot.png" width="500">

*The dashboard shown in its idle state — sensor readings populate live once connected to the robot.*
## Files

| File | Purpose |
|---|---|
| `dashboard.py` | Main controller. Runs the sensor loop, the drive state machine, and a small HTTP server (port 8080) that serves the dashboard and accepts control commands. |
| `dashboard.html` | Browser dashboard: live sensor readings, start/stop/emergency-stop controls, tunable speed/turn/duration sliders, section-by-section drive history. |

## Hardware this expects

- Raspberry Pi 4 Model B, BCM GPIO numbering
- 1× VL53L0X Time-of-Flight sensor on the default I²C bus, address `0x29` (rear)
- 2× ultrasonic distance sensors (left: TRIG BCM5 / ECHO BCM6, right: TRIG BCM20 / ECHO BCM21)
- 1× 3-wire hobby servo (signal BCM12, 50 Hz) — no position feedback
- 1× H-bridge motor driver (EN/PWM on BCM13, IN1 on BCM23, IN2 on BCM24)

Full pin table and the reasoning behind each connection: [`schemes/wiring-diagram.svg`](../../schemes/wiring-diagram.svg).

## Dependencies

```bash
pip install adafruit-circuitpython-vl53l0x adafruit-blinka RPi.GPIO
```

## Running it

1. Place `dashboard.py` and `dashboard.html` in the **same folder** on the Pi, as `/home/sunbird/dashboard.py` and `/home/sunbird/dashboard.html` — the path is hardcoded in `dashboard.py` (`HTML_PATH`), so the HTML file must sit at exactly that path or you'll need to edit that constant.
2. SSH into the Pi and run:
   ```bash
   python3 dashboard.py
   ```
3. Open `http://raspberrypi.local:8080` (or the Pi's IP) in a browser on the same network.
4. **Raise the drive wheels off the ground before the first Start** — see the safety checklist in the root README.

## Safety behavior already built in

- If the browser stops sending its once-per-second heartbeat for more than 3 seconds, the robot force-stops and recenters the steering automatically.
- The motor is always commanded to stop before any steering change.
- `Ctrl+C` / `SIGTERM` triggers a clean shutdown: stop motor, recenter servo, stop PWM, release GPIO.

## Known limitations (intentional, documented in code)

- Speed and distance are **open-loop estimates** (`estimated_speed = max_speed_cm_s × pwm% / 100`, integrated over time) — there is no wheel encoder, so these numbers are not ground truth.
- The servo has no position feedback; the dashboard shows the *commanded* angle only.
