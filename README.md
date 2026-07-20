
<h1 align="center">Sunbird Nomads</h1>

<h3 align="center">
WRO 2026 Future Engineers · Palestine 🇵🇸
</h3>

<p align="center">
  <img src="docs/sunbird-nomads-logo.png"
       alt="Sunbird Nomads team logo"
       width="300">
</p>

<p align="center">
An autonomous vehicle engineered through testing, failure, redesign, and continuous improvement.
</p>

---

##  Repository Contents

| Folder | Contents |
|---|---|
| [`t-photos/`](t-photos/) | Official and informal team photos |
| [`v-photos/`](v-photos/) | Vehicle photographs from every required angle |
| [`video/`](video/) | Driving demonstration videos |
| [`schemes/`](schemes/) | Electrical and wiring diagrams |
| [`src/`](src/) | Testing and final robot software |
| [`models/`](models/) | 3D-printing and CAD files |
| [`docs/`](docs/) | Engineering diagrams and detailed investigations |

---
##  Why “Sunbird Nomads”?

The **Palestine sunbird** is a small, colourful bird native to our region and recognized as the national bird of Palestine. For Palestinians, it represents our land, identity, freedom, and resilience.

The word **Nomads** reflects our engineering journey constantly exploring, adapting, learning, and moving toward better solutions.

Together, **Sunbird Nomads** represents a Palestinian team deeply rooted in its homeland while continuing to move forward and discover new possibilities.

---
## Our Journey

We are **Alma Alkhader** and **Sara Afifi**, two second-year engineering students at Birzeit University brought together by a shared interest in robotics. This is our second year competing in the WRO Future Engineers category. Our experience began with our [WRO 2025 BiruniVerse project](https://github.com/AlmaAlkhader/WRO2025-BiruniVerse), where we gained our first practical experience designing, building, and programming an autonomous vehicle.

###  Meet the Team

<table>
  <tr>
    <th width="50%">Alma Alkhader</th>
    <th width="50%">Sara Afifi</th>
  </tr>
  <tr>
    <td align="center">
      <img src="docs/alma-alkhader.jpg"
           alt="Alma Alkhader"
           width="280">
    </td>
    <td align="center">
      <img src="docs/sara-afifi.jpg"
           alt="Sara Afifi"
           width="280">
    </td>
  </tr>
  <tr>
    <td valign="top">
      <strong>Occupation:</strong> Computer Engineering student<br><br>
      <strong>Academic level:</strong> Second year<br><br>
      <strong>Membership:</strong> IEEE Robotics and Automation Society (RAS), Birzeit University Student Branch<br><br>
      <strong>Interest:</strong> Robotics and autonomous systems<br><br>
      <strong>Team responsibilities:</strong> Power system, electronics, wiring, sensor integration, Raspberry Pi setup, and control software
    </td>
    <td valign="top">
      <strong>Occupation:</strong> Mechanical Engineering student<br><br>
      <strong>Academic level:</strong> Second year<br><br>
      <strong>Membership:</strong> Technical member of IMechE at Birzeit University<br><br>
      <strong>Specialization:</strong> Mechanical design and manufacturing<br><br>
      <strong>Team responsibilities:</strong> Chassis development, steering mechanism, component placement, measurements, and custom-designed mounts
    </td>
  </tr>
</table>

Our different specializations allowed us to approach the robot from two connected perspectives. Alma concentrated on making the electronics and software work reliably, while Sara focused on ensuring that the mechanical design could support those systems and move effectively. Nearly every improvement required both sides to work together.

Our first robot of the 2026 season came to life on **May 19, 2026**, powered by an ESP32. Although it completed the Open Challenge, it still faced major issues with steering, power delivery, and the rear axle. Over the following weeks, we redesigned and improved these systems while balancing the project with our university exams and coursework.

By the local competition on **July 13, 2026**, the robot had evolved significantly. After moving from the ESP32 to a Raspberry Pi and making several mechanical and electrical improvements, it achieved the maximum score in the Open Challenge. We earned **second place** and qualified for the national competition.

We are proud of how far the robot has come, but our journey is not finished. Every test, mistake, and redesign has taught us something new, and we are continuing to improve the robot as we prepare for the next stage of the competition.

## Design Strategy

Our robot is built on a **4WD Arduino RC car chassis**, which we chose as a reliable starting point that allowed us to focus on developing and improving the robot for the WRO Future Engineers competition.

While the kit provided a solid foundation, it also presented several challenges:

* **Limited space** for mounting electronic components, requiring us to carefully redesign the layout and create custom 3D-printed mounts.
* **Minimal assembly documentation**, which led us to reverse-engineer parts of the chassis and solve several mechanical issues during development.

As the project evolved, we continuously modified the original design to better meet the competition's requirements, improving the mechanical structure, electronics integration, and overall reliability.

For future iterations, we plan to redesign the bottom chassis plate to improve the overall structure of the robot. The new design will provide additional clearance for the steering mechanism, enabling a larger steering angle and improved maneuverability during the Obstacle Challenge. Additionally, we aim to make the chassis more modular and accessible, simplifying the assembly and disassembly process while making maintenance and future upgrades easier.
# Hardware Design
## Chassis

Our robot is based on the **4WD Arduino RC Car Chassis**, which provided a solid mechanical foundation, offering rear wheel drive. However, the original design offered very little space for the electronics required for the competition.

To overcome this limitation, we designed a completely new **top mounting plate** and added an **additional layer** to accommodate all of the robot's electronic components while maintaining a compact and organized layout.

<p align="center">
  <img src="image.png" alt="Original 4WD Arduino RC Car Chassis" width="500"/>
  <br>
  <em>Original 4WD Arduino RC Car Chassis used as the base of our robot.</em>
</p>

After identifying all the required electronic components and taking precise measurements, we designed a custom mounting plate tailored to our needs. The design went through **four iterations**, with each version improving the placement of components, cable management, and accessibility until we reached the final design.

<table align="center">
  <tr>
    <td align="center">
      <img src="image-4.png" alt="Middle PLate" width="300" height="300"><br>
      <em>Early prototype</em>
    </td>
    <td align="center">
      <img src="image-3.png" alt="Top plate" width="300" height="300"><br>
      <em>Final design</em>
    </td>
  </tr>
</table>

<p align="center">
  <em>Middle and top layer plates</em>
</p>

## Steering Calibration

One advantage of the chassis kit we used is that it allows adjustments to the steering geometry by changing the lengths of the steering rods. We utilized this flexibility to implement an **Ackermann steering mechanism**, where the inner wheel turns at a greater angle than the outer wheel during cornering.

<p align="center">
  <img src="image-6.png" alt="Ackermann steering mechanism" width="500"/>
</p>

This difference in steering angles is necessary because the inner and outer wheels follow different turning radii. The inner wheel travels along a smaller radius, requiring a larger steering angle to ensure that all wheels rotate around the same instantaneous center of rotation.

To determine the required steering angle for **low-speed cornering**, where tire slip can be neglected, we used the following relationship:

```text
δ = atan(L / R)
```

Where:

```text
δ = steering angle of the vehicle centerline
L = wheelbase
R = turning radius
```

For our robot, we measured:

```text
L = 137 mm
R = 525 mm
```

Substituting these values:

```text
δ = atan(137 / 525)
δ = 14.6°
```

After converting the result from radians to degrees, the required steering angle was approximately **15°**.

We then calibrated the steering mechanism by adjusting the steering rods until the wheels achieved the desired Ackermann geometry, with approximately a **15° steering angle** for the centerline turn.

## Mounts

To ensure reliable performance during the competition, important components such as the **Pi Camera** and distance sensors required custom-designed mounts to keep them securely positioned while maintaining accessibility and accuracy.

### ToF Sensor Mount — Initial Design

Our first approach was to use **Time-of-Flight (ToF) sensors** for obstacle detection. After several design iterations, we developed a dedicated mount that provided a stable position and proper alignment for the sensors.

<p align="center">
  <img src="image-8.png" alt="ToF sensor mount design" width="500"/>
  <br>
  <em>Initial ToF sensor mount design.</em>
</p>

However, during testing, we discovered that ToF sensors were not ideal as our main wall sensors in the WRO mat environment. Their infrared-based measurements were affected by dark surfaces and target geometry. We therefore replaced the side-facing ToF plan with ultrasonic wall sensing, while retaining one rear VL53L0X for short-range parking alignment.

### Ultrasonic Sensor Mount — Final Design

After evaluating different sensor options, we switched to **ultrasonic sensors**, which required a new mounting solution.

<p align="center">
  <img src="image-9.png" alt="Ultrasonic sensor mount design" width="500"/>
  <br>
  <em>Final ultrasonic sensor mount design.</em>
</p>

This design uses a **friction-fit mechanism** to securely hold the sensor in place, eliminating the need for screws while making installation and adjustments faster and easier.

### Pi Camera Mount

The camera is one of the most important components for navigation, requiring a stable and precise mounting position. We designed a dedicated mount that keeps the camera firmly fixed while providing an unobstructed field of view for the lens.

<p align="center">
  <img src="image-10.png" alt="Pi Camera mount design" width="500"/>
  <br>
  <em>Custom Pi Camera mount positioned at the front of the robot.</em>
</p>

The mount secures the camera using screws and includes an opening for the lens. It is installed vertically on the robot's second level, facing forward with its optical axis approximately parallel to the field. This gives it an unobstructed view of the red and green traffic pillars. The **"SN"** engraved on our mounts refers to our team name, **Sunbird Nomads**.

# Power & Sensor Architecture

Our electrical design separates the noisy, high-current drive system from the Raspberry Pi's processing supply. A three-cell motor battery powers the H-bridge, drive motor, and steering-servo rail, while a dedicated USB power bank powers the Raspberry Pi 4 and camera. The two sources share a common ground so that the Raspberry Pi's control signals have the same electrical reference as the H-bridge and servo.

This section distinguishes between **verified configuration**, **manufacturer specifications**, and **measurements still pending**. A value is not presented as a test result unless we recorded it on the robot.

## System Architecture

```mermaid
flowchart TD
    B["3S 18500 battery pack"] --> S1["Drive power switch"]
    S1 --> H["Kit H-bridge"]
    H --> M["12 V kit drive motor"]
    H --> V5["H-bridge module 5 V terminal"]
    V5 --> SV["Steering servo"]

    PB["Billboard 10,000 mAh power bank<br/>5 V / 3 A output"] --> PI["Raspberry Pi 4"]
    PI --> CAM["Arducam 12 MP IMX708 camera"]
    PI --> US["Left and right ultrasonic sensors"]
    PI --> TOF["Rear VL53L0X parking sensor"]
    PI --> H
    PI --> SV
```

The power switch energizes the drive system. A separate start control launches the autonomous program, allowing the robot to be powered and checked before motion begins.

## Power Sources and Distribution

| Source or rail | Connected loads | Confirmed information | Engineering status |
|---|---|---|---|
| 3S motor pack | H-bridge, drive motor, servo rail | 3 × 18500 Li-ion cells, each labelled 3.7 V and 2250 mAh | Pack label and series calculation documented |
| USB power bank | Raspberry Pi 4, camera, Pi-side sensors | Billboard 10,000 mAh; labelled output reported as 5 V / 3 A | Output rating matches the Raspberry Pi 4 supply recommendation; rail-voltage testing pending |
| H-bridge motor output | 12 V kit motor | PWM speed and direction control | Driver marking and motor current pending |
| H-bridge module 5 V terminal | Steering servo | Servo power and ground; signal from Raspberry Pi GPIO12 | Whether the terminal is regulated output or external input must be verified from the board jumper and marking |
| Raspberry Pi 3.3 V and GPIO | Sensor logic | Common ground through the breadboard negative rail | Sensor module revisions and signal voltages must be verified |

The Raspberry Pi 4 requires a good-quality **5 V, 3 A** USB-C supply according to its [official datasheet](https://pip.raspberrypi.com/documents/RP-008341-DS-raspberry-pi-4-datasheet.pdf). The power bank's output rating therefore meets the required supply capability on paper, but its voltage must still be checked while the camera and processor are active.

### 3S Motor-Battery Calculation

The cells are connected in series. Series connection adds voltage, but it does **not** add ampere-hour capacity:

```text
Nominal pack voltage = 3 × 3.7 V = 11.1 V
Fully charged voltage = 3 × 4.2 V = 12.6 V
Pack capacity = 2.25 Ah
Nominal stored energy = 11.1 V × 2.25 Ah = 24.975 Wh ≈ 25.0 Wh
```

The motor is sold as part of a 12 V robot kit, so a 3S lithium-ion pack is electrically close to its intended voltage range: approximately 12.6 V when full and 11.1 V at nominal charge. The actual voltage reaching the motor is lower because the H-bridge has an internal voltage drop.

### H-Bridge Trade-off and Voltage Loss

The driver has been reported as **L928N**, but the exact board and IC marking still require a clear photograph. The commonly supplied module in this type of kit is the **L298N**; therefore, the following calculation is a design check to use **only if the marking confirms L298/L298N**.

The [STMicroelectronics L298 datasheet](https://www.st.com/resource/en/datasheet/l298.pdf) specifies a total bridge saturation-voltage drop of approximately **1.8 V typical and up to 3.2 V at 1 A**. At a nominal 11.1 V pack voltage:

```text
Motor voltage ≈ battery voltage − bridge drop
Best reference case: 11.1 V − 1.8 V = 9.3 V
High-drop case:      11.1 V − 3.2 V = 7.9 V
```

The corresponding driver heat at 1 A is approximately:

```text
Driver loss = current × voltage drop
             = 1 A × (1.8 to 3.2 V)
             = 1.8 to 3.2 W
```

This older bipolar driver is simple and readily available, but it sacrifices motor voltage and produces more heat than a modern MOSFET driver. We retained the kit driver because it was already integrated and sufficient for initial low-speed testing; motor current, heatsink temperature, and loaded motor voltage will determine whether it remains suitable.

## Power Budget

A valid power budget cannot be completed from battery capacity alone. It requires the running and peak current of each load. The table below records the available reference values and what still has to be measured.

| Load | Supply | Datasheet or label value | Robot measurement | Why it matters |
|---|---:|---:|---:|---|
| Raspberry Pi 4 system | 5 V | 3 A recommended supply capability | Pending: idle and camera-active rail voltage | Detects power-bank or cable voltage sag |
| Arducam IMX708 camera | From Pi | Included in Pi-side load | Pending: resolution, frame rate, and Pi rail under streaming | Vision increases processor and supply load |
| Left HC-SR04-type sensor | Presently 3.3 V | Standard HC-SR04 reference: 15 mA at 5 V | Pending: exact board revision, VCC, Echo-high voltage, current | Confirms 3.3 V compatibility and GPIO safety |
| Right HC-SR04-type sensor | Presently 3.3 V | Standard HC-SR04 reference: 15 mA at 5 V | Pending: exact board revision, VCC, Echo-high voltage, current | Same check as left sensor |
| Rear VL53L0X | Pi sensor rail | Bare sensor: 19 mA typical active, 40 mA possible peak | Pending on the installed module | Breakout-board regulator and pull-ups affect actual input current |
| Steering servo | H-bridge 5 V terminal | Unknown kit model | Pending: running and stall current | Usually the largest short-duration 5 V load |
| Drive motor | 3S through H-bridge | Unknown kit model | Pending: free-running, driving, and stall current | Determines battery, driver, switch, and wire stress |

The HC-SR04 reference values come from the [ElecFreaks HC-SR04 datasheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf). The VL53L0X values come from the [STMicroelectronics datasheet](https://www.st.com/resource/en/datasheet/vl53l0x.pdf). Manufacturer values are used for planning; installed-system measurements are needed for validation.

When the missing currents are measured, the peak-current check will be:

```text
I_peak = I_Pi+camera + I_sensors + I_servo_peak
Headroom (%) = (I_supply − I_peak) / I_peak × 100
```

Because the motor battery and Pi power bank are separate, their runtimes must be calculated independently. The robot's usable runtime is the shorter of the two:

```text
Runtime (h) = usable energy (Wh) × efficiency / average load power (W)
System runtime = min(motor-system runtime, Pi-system runtime)
```

The power bank's advertised **10,000 mAh** alone is not enough for an accurate runtime calculation because that rating is normally specified at the internal cell voltage, while the Pi receives regulated 5 V. Usable output energy and conversion efficiency must be measured or obtained from the exact product label/manual.

## Signal and GPIO Map

| Device | Function | BCM GPIO | Physical pin | Interface |
|---|---|---:|---:|---|
| Left ultrasonic | Trigger | GPIO5 | 29 | Digital output |
| Left ultrasonic | Echo | GPIO6 | 31 | Digital input |
| Right ultrasonic | Trigger | GPIO20 | 38 | Digital output |
| Right ultrasonic | Echo | GPIO21 | 40 | Digital input |
| Rear VL53L0X | SDA | GPIO2 | 3 | I²C data |
| Rear VL53L0X | SCL | GPIO3 | 5 | I²C clock |
| Steering servo | PWM signal | GPIO12 | 32 | 50 Hz PWM |
| H-bridge enable | Motor speed | GPIO13 | 33 | 1 kHz PWM |
| H-bridge IN1 | Motor direction | GPIO23 | 16 | Digital output |
| H-bridge IN2 | Motor direction | GPIO24 | 18 | Digital output |

All grounds are currently joined on the breadboard negative rail. This common reference is necessary because the Pi sends control signals to devices powered from the motor-side supply. The final build must also secure the rail connections against vibration and accidental pull-out.

## Sensor Roles, Selection, and Placement

| Sensor | Final role | Why it was selected | Main limitation |
|---|---|---|---|
| Left ultrasonic | Measure distance to the left wall and detect openings | Measures by reflected sound, so wall colour has much less influence than on optical ranging | Wide beam can reflect from angled surfaces; can cross-talk with another ultrasonic sensor |
| Right ultrasonic | Measure distance to the right wall and detect openings | Same device type on both sides simplifies comparison and replacement | Requires timing separation and has a 2 cm reference blind zone |
| Rear VL53L0X ToF | Short-range parking alignment | Narrower optical field of view is useful for alignment with the rear parking boundary | Infrared return can depend on target reflectance, angle, and cover-glass crosstalk |
| Arducam 12 MP IMX708 | Detect red and green traffic pillars | High-resolution colour frames support HSV segmentation and pillar-position estimation | Processing full-resolution frames increases latency; fixed focus and lighting changes require validation |

The side ultrasonic sensors are positioned to observe the two field walls while the car moves. Their exact height, setback from the front axle, angle, and distance from the robot centerline will be added from the final robot measurements. These dimensions are necessary because the WRO rubric asks teams to justify placement using field geometry, and because they determine which part of the wall enters each sensor's beam.

The rear ToF sensor is used specifically for **parking**, not front obstacle detection. It measures the remaining rear clearance during the final parking maneuver.

### Placement Constraints from Field Geometry

The [WRO 2026 Future Engineers rules](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Self-Driving-Cars-General-Rules.pdf) define physical targets that directly affect sensor placement:

| Field feature | Rule dimension | Design consequence |
|---|---:|---|
| Interior and exterior walls | 100 mm high | The ultrasonic acoustic center should remain below the wall top and clear of wheels/mounts |
| Traffic pillars | 50 × 50 × 100 mm | Camera resolution must preserve a useful contour for a 50 mm-wide target at the required detection distance |
| Parking boundary elements | 200 × 20 × 100 mm | Rear ToF line of sight must intersect the 100 mm-high element during parking |
| Maximum vehicle envelope | 300 × 200 × 300 mm | Camera and sensor mounts must remain inside the permitted footprint and height |
| Obstacle Challenge track width | 1000 ± 10 mm | Side ranges must cover the relevant wall distance while leaving margin for turns and openings |

The HC-SR04 reference datasheet lists a **15° measuring angle**. Approximating this as a conical beam, its footprint width at target distance $d$ is:

$$W_{US}=2d\tan(15^\circ/2)$$

| Target distance | Approximate ultrasonic footprint width |
|---:|---:|
| 20 cm | 5.3 cm |
| 50 cm | 13.2 cm |
| 100 cm | 26.3 cm |

This explains why an angled wall, corner, wheel, or nearby mount can become the strongest reflector even when it is not directly in front of the sensor. The VL53L0X bare sensor has a specified **25° field of view**, producing an approximate 4.4 cm footprint at 10 cm and 8.9 cm at 20 cm. Its narrower short-range footprint supports the rear parking role, but the final mount must still be measured against the parking-element height.

For camera calibration, a 50 mm pillar's expected image width can be modeled as:

$$w_{pixels}\approx\frac{f_x\times50\text{ mm}}{Z}$$

where $f_x$ is the calibrated horizontal focal length in pixels and $Z$ is pillar distance in millimetres. We will obtain $f_x$ from the final processing resolution instead of assuming that the full 12 MP sensor resolution is used.

### Ultrasonic Timing and Crosstalk Control

The standard HC-SR04 datasheet recommends a measurement cycle longer than **60 ms**. Our code does not trigger both sensors together: it reads the left sensor, waits **60 ms**, then reads the right sensor. Sequential triggering reduces the chance that one receiver mistakes the other sensor's sound burst for its own echo.

The control loop also applies a three-sample median filter. A median rejects one isolated high or low reading without being shifted as strongly as a mean:

```text
Filtered distance = median(last three valid readings)
```

This filtering and delay improve robustness at the cost of a slower sensing update. The current dashboard cycle is intentionally conservative for testing; after the invalid-reading rate is measured, it can be shortened only if reliability remains acceptable.

### HC-SR04 Voltage Compatibility Check

The installed ultrasonic sensors worked when powered from **3.3 V**, and no Echo voltage divider is currently installed. However, the commonly published HC-SR04 datasheet specifies **5 V operation**, while Raspberry Pi GPIO uses a **3.3 V I/O rail**. There are also newer or compatible ultrasonic-board revisions that accept 3.3–5 V, so visual similarity alone cannot identify the electrical specification.

Before the final wiring is frozen, we will:

1. Photograph and record the exact markings on both sensor PCBs.
2. Measure VCC at each sensor.
3. Trigger a sensor repeatedly and measure the Echo pulse peak with an oscilloscope or logic analyser; an ordinary multimeter may average the short pulse and miss its true peak.
4. If the board schematic or pulse measurement shows that Echo can reach 5 V, add a correctly designed divider or level shifter before the Pi input.
5. Repeat known-distance tests after the protection is installed.

“It works at 3.3 V” is useful experimental evidence, but it does not by itself prove that every module revision will be accurate or reliable at that voltage.

## Camera Hardware and Colour Pipeline

The current upgrade is an **Arducam 12 MP IMX708 fixed-focus HDR camera**. Arducam specifies a maximum sensor resolution of **4608 × 2592**, a 1.4 µm pixel size, and a fixed-focus range listed as 1.5 m to infinity for this module family in its [IMX708 documentation](https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708/). Our task does not require full-resolution recording; it requires low-latency, reliable colour detection. A lower processing resolution will therefore likely be the better trade-off once latency tests are complete.

The existing colour-detection program uses **Picamera2** for capture and **OpenCV** for BGR-to-HSV conversion and contour detection. The currently recorded code values are:

| Parameter | Current code value | Status |
|---|---|---|
| Green HSV lower bound | `[115, 200, 100]` | Implemented; must be retuned/verified on the IMX708 |
| Green HSV upper bound | `[160, 255, 180]` | Implemented; must be retuned/verified on the IMX708 |
| Red HSV lower bound | `[0, 80, 60]` | Implemented; lighting validation pending |
| Red HSV upper bound | `[30, 255, 255]` | Implemented; lighting validation pending |
| Minimum contour area | `800 px²` | Implemented; depends on processing resolution and distance |
| Loop delay | `0.05 s` | Implemented; total measured latency pending |
| Resolution and frame rate | Pending from final detection code | Must be logged, not inferred from sensor maximum |
| Exposure and white balance | Pending from final detection code | Automatic settings can shift HSV values between frames |

Picamera2 is the current Python interface to Raspberry Pi's `libcamera`-based camera stack, as described in the [official Raspberry Pi camera documentation](https://www.raspberrypi.com/documentation/computers/camera_software.html). The new camera is now producing detections; the final code and measured performance will be added after the current detection program is supplied.

## Recorded Integration Observations

These are the exact values retained from earlier individual hardware checks. They confirm communication, but the true target distances were not recorded, so they cannot be used to claim accuracy.

| Device | Recorded observation | What it proves | What it does not prove |
|---|---:|---|---|
| VL53L0X | 159 mm, followed by changing readings | I²C initialization and live ranging worked | Accuracy, parking repeatability, or surface independence |
| Left ultrasonic | Approximately 47–49 cm | Trigger/Echo path returned plausible changing data | Error at a known distance or invalid-reading rate |
| Right ultrasonic | 8.9 cm | Individual sensor read worked at short range | Cross-sensor consistency or calibrated accuracy |

## Validation Plan and Metrics

The complete reproducible procedure and blank raw-data tables are in [`docs/power-sensor-validation.md`](docs/power-sensor-validation.md). Each result table will contain the test date, code commit, battery state, target material, true distance, and all 20 raw readings.

For every target distance and surface, we will calculate:

$$
\text{Mean} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

$$
\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|x_i-x_{true}|
$$

$$
\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2}
$$

We will also report the median and count every timeout, out-of-range value, or physically impossible jump as an invalid reading.

| Test group | Conditions | Metrics | Current status |
|---|---|---|---|
| Ultrasonic accuracy | Black wall, white surface, red pillar, green pillar, flat target, angled target; 20 readings per distance | Mean, median, MAE, standard deviation, invalid count | Protocol ready; raw measurements pending |
| Ultrasonic crosstalk | Simultaneous trigger, sequential trigger, sequential with current 60 ms delay | Incorrect and invalid readings per method | Protocol ready; measurements pending |
| Rear ToF parking | Several known rear clearances and target angles | Offset, MAE, standard deviation, invalid count, stopping repeatability | Protocol ready; measurements pending |
| Camera | Bright, normal, and dim lighting | Minimum detection distance, false positives, false negatives, per-frame latency | Camera detects; controlled dataset pending |
| Pi power | Idle, camera streaming, and full software load | 5 V rail, undervoltage events, runtime, CPU temperature | Multimeter available; measurements pending |
| Drive power | Startup, straight driving, full-left/right steering | Pack voltage, motor voltage, servo rail, driver temperature, resets | Measurements pending |

## Failure-Point Analysis

| Failure mode | Effect on robot | Present control | Required verification or improvement |
|---|---|---|---|
| Servo current spike pulls down H-bridge 5 V rail | Steering jitter, sensor reset, or control instability | Pi has a separate power bank | Measure servo rail during full-left/full-right motion; identify servo current; consider a dedicated regulator if sag or heat appears |
| H-bridge 5 V terminal used in the wrong jumper configuration | Regulator conflict or loss of servo power | None documented | Photograph jumper and board labels; determine whether 5 V pin is input or output before finalizing wiring |
| Standard 5 V Echo reaches Pi GPIO | Possible GPIO damage | Sensors presently powered at 3.3 V | Identify exact sensor revision and measure Echo-high voltage; add level shifting if required |
| Two ultrasonic bursts overlap | False wall distance and incorrect turn decision | Sequential reads with 60 ms separation; median-of-three filter | Complete comparative crosstalk test and publish invalid counts |
| L298-type driver voltage drop and heating | Reduced motor torque/speed or thermal shutdown | Heatsink on common module; conservative PWM | Confirm IC, measure loaded drop and temperature after repeated runs |
| Motor startup noise enters signal ground | False readings or controller reset | Separate Pi power source; common reference ground | Log sensor readings and Pi undervoltage state during motor startup; improve routing/decoupling if correlated errors occur |
| Loose jumper wire or breadboard rail connection | Intermittent sensor, servo, or ground | Visual inspection | Record wire type/gauge, add strain relief and locking connectors where possible |
| Camera exposure/AWB shifts HSV colours | Missed or incorrect pillar classification | HSV thresholds and contour-area filter | Freeze or bound controls after lighting tests; publish confusion counts |
| Unprotected 3S cell pack is overcharged, over-discharged, imbalanced, or shorted | Cell damage, heating, fire risk, or sudden shutdown | Main switch only; no BMS or fuse currently reported | High-priority redesign: verify cells/holder and add correctly rated 3S protection, balanced charging, and overcurrent protection with qualified supervision |

The switch is useful for isolation, but it is **not** a substitute for a battery-management/protection circuit or fuse. Until the pack construction and charging arrangement are reviewed, the absence of a BMS and overcurrent protection remains the highest-priority electrical risk in the current design.

## Immediate Next Measurements

1. Photograph the H-bridge front/back, its jumpers, the servo label, both ultrasonic PCBs, battery holder, switch, and all power-bank labels.
2. Measure the three individual cell voltages and total pack voltage before and after a run; do not short or probe adjacent terminals simultaneously.
3. Measure Pi 5 V rail at idle and while camera detection runs, and record any undervoltage warning.
4. Measure servo rail at center and during repeated full-left/full-right commands; stop if the regulator or servo becomes unusually hot.
5. Measure motor-battery voltage at rest and while driving, then record H-bridge heatsink temperature after repeated runs.
6. Run the prepared 20-reading sensor matrix and crosstalk comparison.
7. Supply the final camera-detection code so resolution, frame rate, camera controls, and latency can be documented exactly.

## 🚀 Software Architecture & Obstacle Strategy

To test and calibrate the robot, we built a live browser dashboard that runs alongside the control code on the Raspberry Pi — showing sensor readings, drive state, and steering in real time, with manual override controls for tuning before autonomous runs.

<img src="docs/dashboard-screenshot.png" width="500">

*The dashboard shown in its idle state — sensor readings populate live once connected to the robot.*

**This is a testing and calibration build for the Open Challenge (Task 1), not our final code** — see [`src/testing/`](src/testing) for the full source and [`src/final/`](src/final) for where the competition version will go.

### Drive state machine

The robot runs as a simple state machine rather than a continuous control loop:

```mermaid
flowchart LR
    stopped -->|Start pressed| forward
    forward -->|turn confirmed| turn_steer
    turn_steer -->|servo settled, 0.45s| turn_drive
    turn_drive -->|turn_duration elapsed| turn_recenter
    turn_recenter -->|servo settled, 0.45s| forward
    forward -->|Stop / Emergency| stopped
```

Every phase transition explicitly stops the motor first, moves the servo, waits for it to physically settle, then resumes — this was a deliberate choice over changing steering angle while still driving, since accessories mounted this close to the servo left very little margin for the wheel to catch a mount mid-turn.

### Turn decision — the math

Every ~340 ms sensor cycle, both ultrasonic readings are median-filtered (window of 3, to reject single-sample noise), giving left distance $L$ and right distance $R$ in cm. We compute:

$$\Delta = |L - R|, \qquad r = \frac{\max(L,R)}{\max(\min(L,R),\ 1)}$$

A turn is only considered when:

$$\Delta \geq 35 \text{ cm} \quad \text{OR} \quad (\Delta \geq 20 \text{ cm} \ \text{AND} \ r \geq 1.8)$$

The ratio clause exists because a fixed centimeter threshold alone misses proportionally large gaps at short range — 15 cm vs. 30 cm ($\Delta=15$) is a real opening but falls under a flat 20 cm cutoff, while 20 cm vs. 40 cm ($\Delta=20,\ r=2.0$) clearly should trigger. Combining both catches that case without lowering the flat threshold enough to react to noise.

Even when the threshold is crossed, the robot doesn't turn immediately — it requires **3 consecutive sensor cycles** to agree on the same direction before committing, and at least **1.5 seconds** of forward driving since the last decision. Both are debounce measures: the first against a single noisy reading, the second against immediately re-triggering right after finishing a turn.

Once committed, it's a **timed maneuver, not a sensor-confirmed exit**: stop → steer → drive for a fixed duration → stop → recenter → resume. The turn doesn't end because the sensors say it's clear; it ends because the clock says so. This is simpler and more predictable to tune than closing the loop on sensor feedback, at the cost of needing the timing recalibrated if speed or the track layout changes.

### Steering angle → servo duty cycle

The servo is commanded by PWM duty cycle, mapped linearly from the calibrated angle range:

$$\text{duty}\% = 2.5 + \frac{\theta - 30}{120}\times 10$$

| Position | Angle | Duty cycle |
|---|---|---|
| Left | 81° | 6.75% |
| Center | 106° | 8.83% |
| Right | 131° | 10.92% |

### Safety systems

- **Heartbeat watchdog:** the browser sends a signal once per second; if it's missing for **3 seconds**, the robot force-stops and recenters automatically, whether or not anyone pressed a button.
- **Motor always stops before steering changes** — never commanded to turn and drive in the same instant.
- **Clean shutdown on Ctrl+C / SIGTERM:** stop motor, recenter servo, stop PWM, release GPIO.

### Known constraints (by design, not oversight)

- Speed and distance are **open-loop estimates** — `estimated_speed = max_speed_cm_s × pwm% / 100`, integrated over time. There's no wheel encoder, so these numbers are useful for tuning consistency but aren't ground truth.
- The servo has no position feedback; the dashboard shows the *commanded* angle only, never a measured one.

## 🧭 Systems Thinking & Engineering Decisions

Every version of this robot exists because an earlier version failed at something specific. This section is the honest version of that story — what we planned, what actually happened, and why we changed course each time.

<img src="docs/engineering-timeline.svg" width="900">

### The plan we started with vs. the robot that actually exists

Early in the season we scoped an ambitious electrical architecture. Most of it didn't survive contact with real hardware — and that's a normal part of engineering, not a failure to hide.

| Subsystem | Original plan | What we're actually running | Why it changed |
|---|---|---|---|
| Motor driver | BTS7960 (high-current) | Kit H-bridge, reported as L928N; exact marking pending | The simpler driver reduced wiring complexity; loaded current, voltage drop, and temperature still need verification |
| Distance sensing | 3× VL53L0X ToF via TCA9548A multiplexer | 1× rear VL53L0X + 2× ultrasonic (left/right) | The multiplexed ToF setup failed to initialize reliably over I²C, *and separately* ToF readings proved unreliable near the mat's black surfaces — two independent reasons pointing the same direction |
| Orientation sensing | MPU6050 IMU | Not present | Cut for now to reduce integration surface while the core drive loop was still being stabilized |
| Power | Protected 3S pack, dual-pack rotation, BMS, two buck converters (5 V logic / 5.5 V servo) | 3S 18500 pack + USB-C power bank (Pi), servo supplied from the H-bridge module's 5 V terminal | Separate motor/Pi sources reduce conducted noise, but the present unprotected cell pack and unverified servo rail remain high-priority risks |


We're not presenting the original plan as a mistake — it was the correct engineering target. What changed is that we chose reliability and debuggability under a real deadline over sophistication we couldn't yet fully verify. That trade-off itself is the point of this section.

### Problems encountered — and what we did about each one

**1. ToF sensors were the wrong tool for this mat, twice over.**
Our first plan used three ToF sensors sharing one connection through a multiplexer chip. That setup never worked reliably. Separately, we also found that even a single, correctly-working ToF sensor struggled near the mat's black surfaces — it measures distance by reflecting infrared light, and black absorbs infrared instead of bouncing it back. Two different problems, same answer: we switched to ultrasonic sensors, which use sound instead of light and don't care what color the wall is.

**2. A live wiring mistake, caught before it became a bigger one.**
One ultrasonic sensor was briefly wired backwards (power and ground reversed) and started heating up. We caught it, disconnected it immediately, and rewired it correctly — it's worked fine since, though we're keeping an eye on it. This is exactly why we treat "every ground wire shares one common rail" as a hard rule everywhere else in this README — it's not caution for caution's sake, it's a lesson from something that actually almost went wrong.

### The pattern across all three

In every case, the fix was to reduce complexity and isolate one failure at a time: fewer sensors on a shared bus instead of debugging a flaky multiplexer, ultrasonic wall sensing instead of relying on infrared reflection, and replacement of the failed IMX219 setup with a working Arducam IMX708 camera. Each decision is recorded so that another team can understand both the current design and the trade-offs still awaiting measurement.
