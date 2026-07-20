# Power and Sensor Validation Protocol

This document defines how Sunbird Nomads will collect repeatable evidence for the robot's power and sensor architecture. Empty result fields mean **not yet measured**; they must not be replaced with assumed values.

## Test Record Header

Copy this block above every new test:

```text
Date and time:
Operator:
Git commit:
Robot configuration:
Motor-pack voltage before test:
Power-bank state:
Room/field lighting:
Ambient temperature:
Notes:
```

## 1. Ultrasonic Accuracy and Repeatability

### Equipment

- Robot with left and right ultrasonic sensors fixed in their competition mounts
- Tape measure or rigid ruler
- Black wall, white flat board, red pillar, and green pillar
- An angled flat target
- Laptop or phone for logging values from the dashboard

### Method

1. Measure from the ultrasonic transducer face, not from the bumper or axle.
2. Place the target at a known perpendicular distance.
3. Keep the robot and target stationary.
4. Record 20 raw readings without discarding timeouts or unexpected values.
5. Repeat for both sensors and every target material.
6. Repeat one target at a deliberate angle and record that angle.
7. Save the raw CSV file with the code commit used during the test.

Recommended initial distances are 10, 20, 30, 50, 75, and 100 cm, limited to distances that fit the actual test space and field geometry.

### CSV Format

```csv
timestamp,sensor,true_distance_cm,surface,mode,reading_cm,valid,notes
2026-07-21T15:00:00,left,20,black_wall,sequential_60ms,20.1,1,
```

Use `valid=0` and leave `reading_cm` empty for a timeout. Do not remove invalid rows.

### Metrics

For valid readings $x_i$ and known distance $x_{true}$:

$$\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$$

$$\mathrm{MAE}=\frac{1}{n}\sum_{i=1}^{n}|x_i-x_{true}|$$

$$\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2}$$

Report the mean, median, MAE, population standard deviation, valid count, invalid count, and invalid percentage. Run:

```bash
python3 src/testing/analyze_sensor_log.py tests/sensor-readings.csv
```

### Results Summary

| Sensor | True distance | Surface | Mean | Median | MAE | Std. dev. | Invalid / 20 |
|---|---:|---|---:|---:|---:|---:|---:|
| Left | Pending | Black wall | Pending | Pending | Pending | Pending | Pending |
| Left | Pending | White surface | Pending | Pending | Pending | Pending | Pending |
| Left | Pending | Red pillar | Pending | Pending | Pending | Pending | Pending |
| Left | Pending | Green pillar | Pending | Pending | Pending | Pending | Pending |
| Left | Pending | Angled surface | Pending | Pending | Pending | Pending | Pending |
| Right | Pending | Black wall | Pending | Pending | Pending | Pending | Pending |
| Right | Pending | White surface | Pending | Pending | Pending | Pending | Pending |
| Right | Pending | Red pillar | Pending | Pending | Pending | Pending | Pending |
| Right | Pending | Green pillar | Pending | Pending | Pending | Pending | Pending |
| Right | Pending | Angled surface | Pending | Pending | Pending | Pending | Pending |

## 2. Ultrasonic Crosstalk Test

### Modes

1. Trigger both sensors as close together as the software allows.
2. Trigger left and right sequentially with no deliberate 60 ms separation.
3. Trigger sequentially using the current 60 ms separation.

### Method

1. Keep the robot centered between two flat walls at measured distances.
2. Record at least 100 left/right sensor pairs per mode.
3. Mark a reading incorrect when it differs from the known distance by more than the acceptance threshold selected before the test.
4. Count timeouts separately from incorrect numeric readings.
5. Repeat with the motor stopped and running to expose possible acoustic/electrical interactions.

| Mode | Sensor pairs | Incorrect left | Incorrect right | Timeouts | Invalid rate | Decision |
|---|---:|---:|---:|---:|---:|---|
| Simultaneous | Pending | Pending | Pending | Pending | Pending | Pending |
| Sequential, no delay | Pending | Pending | Pending | Pending | Pending | Pending |
| Sequential, 60 ms | Pending | Pending | Pending | Pending | Pending | Pending |

## 3. Rear ToF Parking Validation

The rear VL53L0X must be tested in its final mount because sensor offset and cover geometry can affect its reading.

1. Measure the distance from the sensor face to the parking boundary at several clearances.
2. Take 20 readings at every clearance.
3. Repeat against the parking element at 0°, 10°, and 20° relative angle.
4. Repeat the full parking maneuver at least 10 times.
5. Record final physical clearance and whether the car touched a boundary.

| Test | True clearance | Angle | Mean | MAE | Std. dev. | Invalid count |
|---|---:|---:|---:|---:|---:|---:|
| Rear ranging | Pending | 0° | Pending | Pending | Pending | Pending |
| Rear ranging | Pending | 10° | Pending | Pending | Pending | Pending |
| Rear ranging | Pending | 20° | Pending | Pending | Pending | Pending |

| Parking repetition | Final clearance | Contact? | Intervention? | Notes |
|---:|---:|---|---|---|
| 1–10 | Pending | Pending | Pending | Pending |

## 4. Camera Calibration and Detection Test

### Configuration to Record

```text
Camera: Arducam IMX708 12 MP fixed-focus HDR
Capture library: Picamera2
Processing library: OpenCV
Processing resolution:
Frame rate:
Exposure time:
Analogue gain:
Auto exposure enabled/disabled:
Auto white balance enabled/disabled:
Colour gains:
Red HSV range: [0, 80, 60] to [30, 255, 255]
Green HSV range: [115, 200, 100] to [160, 255, 180]
Minimum contour area: 800 px²
```

The HSV values above are the current code settings, not calibration results. Record any changed values together with the image dataset and commit.

### Dataset

For each bright, normal, and dim condition, collect frames containing:

- red pillar only;
- green pillar only;
- both pillars;
- no pillar;
- distracting red/green objects where possible;
- pillars at several distances and image positions.

Manually label the expected result for every frame. A false positive is a detection when the labelled pillar is absent; a false negative is a missed labelled pillar.

$$\text{False-positive rate}=\frac{FP}{FP+TN}$$

$$\text{False-negative rate}=\frac{FN}{FN+TP}$$

Measure processing latency around the complete capture-and-detection step using a monotonic timer. Report median, 95th percentile, and maximum latency rather than only the best frame.

| Lighting | Frames | TP | TN | FP | FN | FP rate | FN rate | Median latency | 95th percentile |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Bright | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending |
| Normal | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending |
| Dim | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending | Pending |

## 5. Power Integrity and Runtime

### Multimeter Tests

Use secure test points and keep probes away from adjacent battery terminals. Do not perform intentional motor- or battery-short tests.

| Measurement | Test condition | Minimum | Typical | Maximum | Reset/undervoltage? |
|---|---|---:|---:|---:|---|
| Pi 5 V rail | Idle | Pending | Pending | Pending | Pending |
| Pi 5 V rail | Camera streaming/detecting | Pending | Pending | Pending | Pending |
| Motor pack | Before startup | Pending | Pending | Pending | N/A |
| Motor pack | Straight driving | Pending | Pending | Pending | Pending |
| Motor output | Straight driving | Pending | Pending | Pending | Pending |
| Servo rail | Centered | Pending | Pending | Pending | Pending |
| Servo rail | Repeated full-left/full-right | Pending | Pending | Pending | Pending |

Check Raspberry Pi undervoltage history after each run:

```bash
vcgencmd get_throttled
```

Record the raw hexadecimal result. A clean present-and-history result is `0x0`; decode any set bits using the Raspberry Pi documentation for the installed OS/firmware version.

### Runtime

1. Fully prepare both power sources using the team's normal safe procedure.
2. Record start time and initial voltages.
3. Run the same repeated workload: camera detection active, sensors reading, steering periodically moving, and the car completing repeatable laps or raised-wheel cycles.
4. Stop at the team's predefined safe battery threshold, any protection shutdown, unstable behavior, or Pi undervoltage.
5. Record elapsed time and final voltages.

| Run | Workload | Start voltage | End voltage | Pi runtime | Motor runtime | Limiting source |
|---|---|---:|---:|---:|---:|---|
| 1 | Pending | Pending | Pending | Pending | Pending | Pending |

## 6. Temperature and Reset Correlation

Record temperature after a fixed-duration run. Use the same measurement point and method every time.

| Component | Before | After 5 min | After 10 min | Maximum | Pass criterion |
|---|---:|---:|---:|---:|---|
| Raspberry Pi CPU (`vcgencmd measure_temp`) | Pending | Pending | Pending | Pending | No throttling |
| H-bridge heatsink | Pending | Pending | Pending | Pending | No shutdown; limit set after board confirmation |
| H-bridge 5 V regulator area | Pending | Pending | Pending | Pending | No abnormal heating or rail sag |
| Steering servo case | Pending | Pending | Pending | Pending | No abnormal heating or jitter |
| Motor case | Pending | Pending | Pending | Pending | No abnormal heating or loss of performance |

During every power test, note whether motor startup or steering causes:

- Raspberry Pi undervoltage or reboot;
- a dashboard disconnect;
- sensor timeouts or jumps;
- servo jitter;
- camera frame loss;
- unexpected H-bridge or regulator heating.

## 7. Evidence Checklist

- [ ] Raw CSV files committed without deleting failed readings
- [ ] Test setup photographs with ruler/target visible
- [ ] Exact code commit recorded for every dataset
- [ ] H-bridge, servo, ultrasonic-board, cell, switch, and power-bank labels photographed
- [ ] Final sensor positions measured from fixed chassis reference points
- [ ] Power and ground wiring photographed from top and bottom
- [ ] Summary tables calculated from raw data
- [ ] Any design change linked to before/after evidence
