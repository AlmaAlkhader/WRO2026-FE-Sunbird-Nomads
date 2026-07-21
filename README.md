
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

<p align="center">
  <img src="docs/why-sunbird-nomads.svg" alt="Visual explanation of the Sunbird Nomads team name" width="900"/>
</p>

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

<p align="center">
  <img src="docs/two-paths-one-robot.svg" alt="Alma's electronics path and Sara's mechanical-design path joining into one robot engineering journey" width="1000"/>
  <br>
  <em>Two specializations developed together through every prototype, redesign, and milestone.</em>
</p>

Our first robot of the 2026 season came to life on **May 19, 2026**, powered by an ESP32. Although it completed the Open Challenge, it still faced major issues with steering, power delivery, and the rear axle. Over the following weeks, we redesigned and improved these systems while balancing the project with our university exams and coursework.

By the local competition on **July 13, 2026**, the robot had evolved significantly. After moving from the ESP32 to a Raspberry Pi and making several mechanical and electrical improvements, it achieved the maximum score in the Open Challenge. We earned **second place** and qualified for the national competition.

We are proud of how far the robot has come. Every test, mistake, and redesign contributed to the final architecture documented in this repository.

## Design Strategy

Our robot is built on a **4WD Arduino RC car chassis**, which we chose as a reliable starting point that allowed us to focus on developing and improving the robot for the WRO Future Engineers competition.

While the kit provided a solid foundation, it also presented several challenges:

* **Limited space** for mounting electronic components, requiring us to carefully redesign the layout and create custom 3D-printed mounts.
* **Minimal assembly documentation**, which led us to reverse-engineer parts of the chassis and solve several mechanical issues during development.

As the project evolved, we continuously modified the original design to better meet the competition's requirements, improving the mechanical structure, electronics integration, and overall reliability.

# Hardware Design
## Mobility and Mechanical Design

The mechanical system uses a conventional car layout: a **single rear drive axle** provides forward and reverse motion, while an **S3003 servo** steers the two front wheels through linkages. This layout satisfies the WRO requirement for a four-wheeled vehicle with one driving axle and one steering actuator, and it behaves more like a road car than a differential-drive robot.

### Chassis and Drive Layout

Our robot is based on the [**RoboticX 4WD RC Smart Car Chassis with S3003 Servo and Bearing Kit**](https://roboticx.ps/product/4wd-rc-smart-car-chassis-with-s3003-metal-servo-bearing-kit-for-arduino/). Despite the product name, the seller describes this chassis as **rear-wheel drive with front-wheel steering**. The kit includes one S3003 steering servo, a 25 mm all-metal gearmotor, a mechanically connected rear axle, bearings, steering rods, and four wheels. The [**L298N dual motor controller**](https://roboticx.ps/product/dual-motor-controller-module-l298n/) was purchased separately.

We selected the kit as a reliable mechanical starting point, but we did not keep its original component layout. Its acrylic plate had limited usable space and mounting holes intended mainly for an Arduino. Our Raspberry Pi, power system, camera, motor controller, and sensors required a new structure, so we designed a custom middle plate and an upper electronics layer.

<p align="center">
  <img src="image.png" alt="Original RoboticX rear-wheel-drive chassis" width="500"/>
  <br>
  <em>Original chassis before adding the custom two-level electronics structure.</em>
</p>

### Final Vehicle Dimensions

| Dimension | Final value | How it was obtained | Why it matters |
|---|---:|---|---|
| Overall length | 248 mm | Measured vehicle length; also matches the chassis listing | Determines WRO envelope margin and parking-space length |
| Chassis width | 146 mm | Published chassis width | Determines lateral clearance and field-centering geometry |
| Assembled height | 126 mm | Measured with the upper electronics layer installed | Confirms that the two-level design remains inside the height limit |
| Wheelbase | 137 mm | Measured axle-to-axle distance | Used in steering-angle calculations |
| Front track width | 117 mm | Measured between the front wheel centerlines | Used to calculate different inner and outer steering angles |
| Wheel diameter | 64 mm | Measured wheel diameter | Determines distance travelled per wheel revolution |
| Ground clearance | 19 mm | Measured from the ground to the lowest chassis surface | Reduces the chance of the plate catching on small field irregularities |

<p align="center">
  <img src="docs/mechanical-overview.svg" alt="Top and side views with the robot's mechanical dimensions and field-fit calculations" width="1000"/>
  <br>
  <em>Final dimensions, WRO size margins, wheel travel, and parking-space calculations.</em>
</p>

The [WRO 2026 rules](https://wro-association.org/wp-content/uploads/WRO-2026-Future-Engineers-Self-Driving-Cars-General-Rules.pdf) limit the vehicle to **300 × 200 mm** and **300 mm in height**. Comparing the final robot with that envelope gives:

```text
Length margin = 300 − 248 = 52 mm
Width margin  = 200 − 146 = 54 mm
Height margin = 300 − 126 = 174 mm
```

These are total envelope margins. They show that the second electronics layer and sensor mounts remain within the dimensional limit without requiring parts to be removed before inspection.

### Wheel Geometry and Linear Travel

With a measured wheel diameter of **64 mm**, the theoretical distance travelled by one complete wheel revolution is:

$$C=\pi D=\pi(64)=201.1\text{ mm}$$

Therefore, one wheel revolution corresponds to approximately **201 mm of linear travel** if tire slip is neglected. Once wheel speed $n$ is measured in revolutions per minute, the theoretical vehicle speed can be calculated using:

$$v=\frac{\pi Dn}{60}$$

where $D$ is expressed in metres and $v$ is obtained in metres per second. This relationship separates the known wheel geometry from motor speed, which must be measured under the robot's actual load rather than assumed from an unidentified motor rating.

### Field-Centering and Parking Geometry

During setup, we established the robot's centerline by measuring from the track walls to the midpoint of the vehicle. For a corridor width $W_t$, a centered robot midpoint is:

$$d_{mid}=\frac{W_t}{2}$$

The open challenge may use a **1000 mm** or **600 mm** corridor, while the obstacle challenge uses a **1000 mm** corridor. The nominal midpoint references are therefore:

| Nominal corridor width | Wall-to-midpoint reference | Side clearance with a 146 mm robot |
|---:|---:|---:|
| 1000 mm | 500 mm | $(1000-146)/2=427$ mm per side |
| 600 mm | 300 mm | $(600-146)/2=227$ mm per side |

The WRO rules allow dimensional tolerance in the field, so these values define the geometry rather than a single inflexible sensor threshold.

For the obstacle challenge, the parking space is **200 mm wide**, and its length is $1.5$ times the vehicle length:

```text
Parking length = 1.5 × 248 = 372 mm
Longitudinal allowance = 372 − 248 = 124 mm
Lateral allowance = 200 − 146 = 54 mm
Centered lateral allowance = 54 / 2 = 27 mm per side
```

The remaining **VL53L0X ToF sensor is mounted at the rear** and is used to monitor the final rear clearance during parking. Its job is separate from the left and right ultrasonic sensors used for wall sensing.

### Custom Plate Development

After identifying the required components, we designed custom middle and top plates to increase usable mounting area while preserving access to wiring and controls. The plate design went through **four physical iterations**. Our initial measurements were not accurate enough to produce a correct fit on the first attempt, so every printed version was installed on the real chassis, checked, remeasured, and revised.

<table align="center">
  <tr>
    <td align="center">
      <img src="image-4.png" alt="Early custom middle plate prototype" width="300" height="300"><br>
      <em>Early prototype</em>
    </td>
    <td align="center">
      <img src="image-3.png" alt="Final custom top plate" width="300" height="300"><br>
      <em>Final design</em>
    </td>
  </tr>
</table>

<p align="center">
  <img src="docs/mechanical-iteration-loop.svg" alt="Measure, model, print, fit-test, and refine loop used across four plate versions" width="1000"/>
  <br>
  <em>The physical fit test converted measurement errors into specific CAD corrections.</em>
</p>

The process was not simply “print until it looks right.” Each loop checked whether components fitted without interference, whether cables could reach without being sharply bent, whether switches remained accessible, and whether the camera and sensors had an unobstructed view. Repeating the cycle improved component placement, cable management, and service access.

### 3D-Printing Configuration

The final plates were produced by FDM printing on an **ELEGOO Centauri Carbon** using **Rapid PETG**. ELEGOO lists PETG as a supported material and specifies a **0.1–0.4 mm** layer-height range for this printer; our **0.12 mm** setting is near the fine-detail end of that range.

| Setting | Final value | Engineering purpose |
|---|---:|---|
| Printer | ELEGOO Centauri Carbon | Enclosed CoreXY FDM printer used for the final plates |
| Material | Rapid PETG | Tougher functional material for plates handled and reassembled repeatedly |
| Layer height | 0.12 mm | Finer vertical resolution and more controlled fit, at the cost of longer print time |
| Wall loops | 3 | Adds perimeter stiffness around the plate edges and mounting holes |
| Sparse infill pattern | Gyroid | Distributes internal support in multiple directions without using solid infill everywhere |
| Sparse infill density | 25% | Balances rigidity, material use, mass, and print time |

Compared with the printer's commonly recommended **0.20 mm** layer height, a 0.12 mm layer produces approximately:

$$\frac{0.20}{0.12}=1.67$$

or **67% more layers for the same part height**. We accepted the longer printing time because dimensional fit and clean mount features were more important than minimum production time for the final plates.

Printer reference: [ELEGOO Centauri Carbon specifications](https://eu.elegoo.com/en-be/products/centauri-carbon).

### Mechanical Design Trade-offs

| Decision | Benefit | Trade-off |
|---|---|---|
| Rear-wheel drive with front steering | Car-like motion and compliance with the WRO mobility rules | Requires steering-link calibration and has a larger turning radius than differential drive |
| Two-level electronics structure | Provides enough mounting area and improves component organization | Raises the assembled height and can raise the center of mass |
| Rapid PETG printed plates | Tough functional parts that can be redesigned and reproduced | Printing at 0.12 mm takes longer, and dimensional errors require reprinting |
| 25% gyroid infill with three walls | Balances stiffness and material use | Not as rigid as a fully solid plate |
| Friction-fit ultrasonic mounts | Fast installation and removal without extra screws | Fit depends strongly on printing accuracy and material tolerance |
| Rear ToF parking sensor | Direct rear-clearance measurement during parking | Adds a dedicated sensor and mount used only in the parking phase |

## Steering Calibration

The chassis allows the steering-rod lengths to be adjusted. We used this to approximate **Ackermann steering**, where the inner front wheel turns more sharply than the outer front wheel because the two wheels follow different radii around the same instantaneous center of rotation.

<p align="center">
  <img src="image-6.png" alt="Ackermann steering mechanism" width="500"/>
</p>

For low-speed cornering, the centerline steering angle is:

$$\delta=\tan^{-1}\left(\frac{L}{R}\right)$$

Using the measured wheelbase $L=137$ mm and turning radius $R=525$ mm:

$$\delta=\tan^{-1}\left(\frac{137}{525}\right)=14.6^\circ\approx15^\circ$$

The measured front track width $t=117$ mm lets us estimate the ideal inner and outer wheel angles:

$$\delta_{in}=\tan^{-1}\left(\frac{L}{R-t/2}\right)
=\tan^{-1}\left(\frac{137}{525-58.5}\right)=16.4^\circ$$

$$\delta_{out}=\tan^{-1}\left(\frac{L}{R+t/2}\right)
=\tan^{-1}\left(\frac{137}{525+58.5}\right)=13.2^\circ$$

| Steering reference | Calculated angle |
|---|---:|
| Vehicle centerline | 14.6° |
| Inner front wheel | 16.4° |
| Outer front wheel | 13.2° |
| Inner-to-outer difference | 3.2° |

We adjusted the steering rods until the wheels followed this geometry as closely as the kit mechanism allowed. This reduces tire scrub compared with forcing both front wheels to the same angle.

## Mounts

The camera and distance sensors use custom-designed mounts so their position does not change during a run while remaining accessible for maintenance.

### ToF Sensor Mount — Initial Design and Final Rear Use

Our first approach used multiple Time-of-Flight sensors for wall sensing. After several design iterations, we produced a stable ToF mount.

<p align="center">
  <img src="image-8.png" alt="ToF sensor mount design" width="500"/>
  <br>
  <em>ToF sensor mount design.</em>
</p>

Testing showed that ToF sensors were not suitable as our main wall sensors on the WRO mat because infrared return varied with dark surfaces and target geometry. We replaced the side-facing ToF plan with ultrasonic wall sensing. **One VL53L0X remains mounted on the back of the vehicle for short-range parking alignment.**

### Ultrasonic Sensor Mount — Final Design

The left and right ultrasonic sensors required a different mount that kept both transducers clear of the chassis.

<p align="center">
  <img src="image-9.png" alt="Ultrasonic sensor mount design" width="500"/>
  <br>
  <em>Final ultrasonic sensor mount design.</em>
</p>

The mount uses a **friction-fit mechanism** to hold the sensor without screws. This makes installation and replacement fast, but it also made print accuracy important: an undersized opening could damage the board, while an oversized opening allowed the sensor angle to change.

### Pi Camera Mount

The camera requires a stable, repeatable position because a change in height or angle changes the apparent location of the traffic pillars. We designed a screw-mounted holder with an unobstructed lens opening.

<p align="center">
  <img src="image-10.png" alt="Pi Camera mount design" width="500"/>
  <br>
  <em>Custom camera mount on the second level at the front of the robot.</em>
</p>

The camera is installed vertically on the second level, facing forward with its optical axis approximately parallel to the field. The **“SN”** engraving identifies the mount as a Sunbird Nomads part.

# Power & Sensor Architecture

Our electrical design separates the noisy, high-current drive system from the Raspberry Pi's processing supply. A three-cell motor battery powers the H-bridge, drive motor, and steering-servo rail, while a dedicated USB power bank powers the Raspberry Pi 4 and camera. The two sources share a common ground so that the Raspberry Pi's control signals have the same electrical reference as the H-bridge and servo.

This section uses the robot's confirmed configuration, values recovered from our project records, and manufacturer specifications. No unrecorded measurement is presented as a test result.

## Main Electrical Components

<table align="center">
  <tr>
    <td align="center" width="33%">
      <img src="docs/components/18500-li-ion-cell.jpg" alt="18500 lithium-ion battery cell" width="250"><br>
      <strong>3 × 18500 Li-ion cells</strong><br>
      <sub>3.7 V, 2250 mAh per cell</sub>
    </td>
    <td align="center" width="33%">
      <img src="docs/components/l298n.png" alt="L298N motor-controller module" width="250"><br>
      <strong>L298N motor controller</strong><br>
      <sub>Purchased separately from the chassis</sub>
    </td>
    <td align="center" width="33%">
      <img src="docs/components/chassis-kit-motor-servo.jpg" alt="Chassis kit containing S3003 servo and 25 millimetre gearmotor" width="250"><br>
      <strong>S3003 servo + 25 mm gearmotor</strong><br>
      <sub>Supplied with the RoboticX chassis</sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub>Component sources: team battery record and the RoboticX <a href="https://roboticx.ps/product/dual-motor-controller-module-l298n/">L298N</a> and <a href="https://roboticx.ps/product/4wd-rc-smart-car-chassis-with-s3003-metal-servo-bearing-kit-for-arduino/">chassis-kit</a> listings.</sub>
</p>

## System Architecture

<p align="center">
  <img src="docs/power-distribution.svg" alt="Power and control distribution diagram" width="900"/>
  <br>
  <em>Confirmed power paths, connected loads, control signals, and shared ground.</em>
</p>

The power switch energizes the drive system. A separate start control launches the autonomous program, allowing the robot to be powered and checked before motion begins.

## Power Sources and Distribution

| Source or rail | Connected loads | Confirmed information |
|---|---|---|
| 3S motor pack | L298N H-bridge, drive motor, servo rail | 3 × 18500 Li-ion cells, each labelled 3.7 V and 2250 mAh |
| USB power bank | Raspberry Pi 4, camera, and Pi-side sensors | Billboard 10,000 mAh, 5 V / 3 A output |
| L298N motor output | 25 mm all-metal gearmotor | PWM speed and direction control |
| H-bridge module 5 V terminal | S3003 steering servo | Servo power and ground; control signal from Raspberry Pi GPIO12 |
| Raspberry Pi 3.3 V and GPIO | Ultrasonic and ToF sensor logic | Common ground through the breadboard negative rail |

The Raspberry Pi 4 requires a good-quality **5 V, 3 A** USB-C supply according to its [official datasheet](https://pip.raspberrypi.com/documents/RP-008341-DS-raspberry-pi-4-datasheet.pdf). The power bank's labelled output matches that supply requirement.

### 3S Motor-Battery Calculation

The cells are connected in series. Series connection adds voltage, but it does **not** add ampere-hour capacity:

```text
Nominal pack voltage = 3 × 3.7 V = 11.1 V
Fully charged voltage = 3 × 4.2 V = 12.6 V
Pack capacity = 2.25 Ah
Nominal stored energy = 11.1 V × 2.25 Ah = 24.975 Wh ≈ 25.0 Wh
```

The 3S pack therefore supplies approximately **12.6 V when fully charged** and **11.1 V at nominal charge**. The voltage reaching the motor is lower because the L298N has an internal voltage drop.

### H-Bridge Trade-off and Voltage Loss

The installed driver is the separately purchased [**RoboticX L298N dual motor-controller module**](https://roboticx.ps/product/dual-motor-controller-module-l298n/). Its seller specifications list a **6–15 V motor-supply range**, **4.5–5.5 V logic range**, **2 A maximum drive current**, and **0–100% output duty cycle**.

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

This older bipolar driver is simple and readily available, but it sacrifices motor voltage and produces more heat than a modern MOSFET driver. We retained it because it was already integrated and provided the required PWM speed and direction control.

## Documented Electrical Load Data

| Load | Supply | Datasheet or seller value | Why it matters |
|---|---:|---|---|
| Raspberry Pi 4 system | 5 V | 3 A recommended supply capability | Establishes the required continuous output of the USB power bank and cable |
| Left HC-SR04-type sensor | Installed at 3.3 V | Standard HC-SR04 reference: 15 mA at 5 V | Distinguishes the installed working configuration from the standard module specification |
| Right HC-SR04-type sensor | Installed at 3.3 V | Standard HC-SR04 reference: 15 mA at 5 V | Uses the same supply and reference as the left sensor |
| Rear VL53L0X | Raspberry Pi sensor rail | Bare sensor: 19 mA typical active and up to 40 mA peak | Accounts for the parking sensor's load on the Pi-side rail |
| L298N motor controller | 3S motor pack | 6–15 V motor supply, 4.5–5.5 V logic, and 2 A maximum drive current | Confirms compatibility with the motor pack and defines the controller's published current limit |

Sources: [Raspberry Pi 4 datasheet](https://pip.raspberrypi.com/documents/RP-008341-DS-raspberry-pi-4-datasheet.pdf), [HC-SR04 reference sheet](https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf), [STMicroelectronics VL53L0X datasheet](https://www.st.com/resource/en/datasheet/vl53l0x.pdf), and [RoboticX L298N product page](https://roboticx.ps/product/dual-motor-controller-module-l298n/).

The power sources are intentionally separated: the 3S pack handles drive and steering loads, while the USB power bank isolates the Raspberry Pi and vision system from motor-current transients.

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

All grounds are joined on the breadboard negative rail. This common reference is necessary because the Pi sends control signals to devices powered from the motor-side supply.

## Sensor Roles, Selection, and Placement

| Sensor | Final role | Why it was selected | Main limitation |
|---|---|---|---|
| Left ultrasonic | Measure distance to the left wall and detect openings | Measures by reflected sound, so wall colour has much less influence than on optical ranging | Wide beam can reflect from angled surfaces; can cross-talk with another ultrasonic sensor |
| Right ultrasonic | Measure distance to the right wall and detect openings | Same device type on both sides simplifies comparison and replacement | Requires timing separation and has a 2 cm reference blind zone |
| Rear VL53L0X ToF | Short-range parking alignment | Narrower optical field of view is useful for alignment with the rear parking boundary | Infrared return can depend on target reflectance, angle, and cover-glass crosstalk |
| Arducam 12 MP IMX708 | Detect red and green traffic pillars | High-resolution colour frames support HSV segmentation and pillar-position estimation | Processing full-resolution frames increases latency; fixed focus reduces near-field sharpness |

### Distance-Sensor Reference Photos

<table align="center">
  <tr>
    <td align="center" width="50%">
      <img src="docs/components/hc-sr04.jpg" alt="HC-SR04 ultrasonic distance sensor" width="300"><br>
      <strong>2 × HC-SR04-type ultrasonic sensors</strong><br>
      <sub>Left and right wall sensing</sub>
    </td>
    <td align="center" width="50%">
      <img src="docs/components/vl53l0x.jpg" alt="VL53L0X time-of-flight sensor module" width="300"><br>
      <strong>1 × VL53L0X ToF sensor</strong><br>
      <sub>Rear parking-distance sensing</sub>
    </td>
  </tr>
</table>

<p align="center">
  <sub>Reference images: <a href="https://instock.pk/hc-sr04-ultrasonic-sensor-distance-measuring-module.html">HC-SR04</a> and <a href="https://store.fut-electronics.com/products/vl53l0x-time-of-flight-sensor-precision-distance-measurements">VL53L0X module</a>.</sub>
</p>

The ultrasonic sensors face left and right so that each one has a direct line of sight to one track wall. This placement supports wall-distance comparison and exposes the sudden open-space reading used to identify corners. The rear-facing ToF sensor is separated from this navigation pair because its role is parking clearance rather than turn detection.

<p align="center">
  <img src="docs/sensor-layout.svg" alt="Conceptual top view of the robot sensor layout" width="900"/>
  <br>
  <em>Conceptual top view showing each sensor's direction and role; component positions are not dimensioned.</em>
</p>

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

Ultrasonic sensors detect objects across a wide area, so they may sometimes pick up nearby wheels, mounts, corners, or angled walls instead of the intended wall. The rear VL53L0X sensor observes a smaller area, making it more suitable for precise parking-distance measurements.

### Ultrasonic Timing and Crosstalk Control

The standard HC-SR04 datasheet recommends a measurement cycle longer than **60 ms**. Our code does not trigger both sensors together: it reads the left sensor, waits **60 ms**, then reads the right sensor. Sequential triggering reduces the chance that one receiver mistakes the other sensor's sound burst for its own echo.

The control loop also applies a three-sample median filter. A median rejects one isolated high or low reading without being shifted as strongly as a mean:

```text
Filtered distance = median(last three valid readings)
```

This filtering and delay improve robustness at the cost of a slower sensing update. The dashboard therefore prioritizes stable wall readings over maximum update rate.

### HC-SR04 Voltage Configuration

The installed ultrasonic sensors operate when powered from **3.3 V**, and no Echo voltage divider is used. This is the robot's observed configuration. The commonly published HC-SR04 reference sheet instead specifies **5 V operation**, while Raspberry Pi GPIO uses a **3.3 V I/O rail**. For that reason, this repository does not generalize the robot's observed 3.3 V behaviour to every HC-SR04 board revision.

## Camera Hardware and Colour Pipeline

The installed camera is an **Arducam 12 MP IMX708 fixed-focus HDR camera**. Arducam specifies a maximum sensor resolution of **4608 × 2592**, a 1.4 µm pixel size, and a fixed-focus range listed as 1.5 m to infinity for this module family in its [IMX708 documentation](https://docs.arducam.com/Raspberry-Pi-Camera/Native-camera/12MP-IMX708/). The camera is used for colour detection rather than full-resolution recording.

The existing colour-detection program uses **Picamera2** for capture and **OpenCV** for BGR-to-HSV conversion and contour detection. The currently recorded code values are:

| Parameter | Current code value |
|---|---|
| Green HSV lower bound | `[115, 200, 100]` |
| Green HSV upper bound | `[160, 255, 180]` |
| Red HSV lower bound | `[0, 80, 60]` |
| Red HSV upper bound | `[30, 255, 255]` |
| Minimum contour area | `800 px²` |
| Loop delay | `0.05 s` |

Picamera2 is the Python interface to Raspberry Pi's `libcamera`-based camera stack, as described in the [official Raspberry Pi camera documentation](https://www.raspberrypi.com/documentation/computers/camera_software.html). The new camera is producing colour detections with the recorded OpenCV pipeline.

## Recorded Integration Observations

These are the exact values retained from earlier individual hardware checks. They confirm communication, but the true target distances were not recorded, so they cannot be used to claim accuracy.

| Device | Recorded observation | What it proves | What it does not prove |
|---|---:|---|---|
| VL53L0X | 159 mm, followed by changing readings | I²C initialization and live ranging worked | Accuracy, parking repeatability, or surface independence |
| Left ultrasonic | Approximately 47–49 cm | Trigger/Echo path returned plausible changing data | Error at a known distance or invalid-reading rate |
| Right ultrasonic | 8.9 cm | Individual sensor read worked at short range | Cross-sensor consistency or calibrated accuracy |

## Failure-Point Analysis

| Failure mode | Effect on robot | Current design response |
|---|---|---|
| Two ultrasonic bursts overlap | False wall distance and incorrect turn decision | Sensors are triggered sequentially with 60 ms separation and a median-of-three filter |
| L298N voltage drop | Reduced motor voltage and power lost as heat | The loss is calculated above and the robot uses conservative PWM settings |
| Motor electrical noise reaches processing electronics | Sensor errors or controller reset | The Raspberry Pi and camera use a separate USB power bank while all control signals retain a common ground reference |
| Camera colour shifts | Missed or incorrect pillar classification | HSV bounds are combined with an 800 px² contour-area threshold |
| Ultrasonic VCC/GND reversed | Sensor heating and possible damage | The earlier incident was stopped immediately; common-rail wiring and pin checks were adopted afterward |
| Unprotected 3S cell pack is overcharged, over-discharged, imbalanced, or shorted | Cell damage, heating, fire risk, or sudden shutdown | The pack has a physical isolation switch, but no BMS or fuse is installed |

The switch is useful for isolation, but it is **not** a substitute for a battery-management/protection circuit or fuse. The absence of a BMS and overcurrent protection is the highest-priority electrical risk in the current design.

## 🚀 Software Architecture & Obstacle Strategy

To test and calibrate the robot, we built a live browser dashboard that runs alongside the control code on the Raspberry Pi — showing sensor readings, drive state, and steering in real time, with manual override controls for tuning before autonomous runs.

<img src="docs/dashboard-screenshot.png" width="500">

*The dashboard shown in its idle state — sensor readings populate live once connected to the robot.*

**This is a testing and calibration build for the Open Challenge (Task 1), not competition code** — see [`src/testing/`](src/testing) for the full source.

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
| Motor driver | BTS7960 (high-current) | L298N H-bridge | The simpler driver reduced wiring complexity and provides the required PWM speed and direction control |
| Distance sensing | 3× VL53L0X ToF via TCA9548A multiplexer | 1× rear VL53L0X + 2× ultrasonic (left/right) | The multiplexed ToF setup failed to initialize reliably over I²C, *and separately* ToF readings proved unreliable near the mat's black surfaces — two independent reasons pointing the same direction |
| Orientation sensing | MPU6050 IMU | Not present | Removed to reduce integration complexity while stabilizing the core drive loop |
| Power | Protected 3S pack, dual-pack rotation, BMS, two buck converters (5 V logic / 5.5 V servo) | 3S 18500 pack + USB-C power bank (Pi), servo supplied from the H-bridge module's 5 V terminal | Separate motor/Pi sources reduce conducted noise; the unprotected cell pack remains the major electrical risk |


We're not presenting the original plan as a mistake — it was the correct engineering target. What changed is that we chose reliability and debuggability under a real deadline over sophistication we could not fully verify. That trade-off itself is the point of this section.

### Problems encountered — and what we did about each one

**1. ToF sensors were the wrong tool for this mat, twice over.**
Our first plan used three ToF sensors sharing one connection through a multiplexer chip. That setup never worked reliably. Separately, we also found that even a single, correctly-working ToF sensor struggled near the mat's black surfaces — it measures distance by reflecting infrared light, and black absorbs infrared instead of bouncing it back. Two different problems, same answer: we switched to ultrasonic sensors, which use sound instead of light and don't care what color the wall is.

**2. A live wiring mistake, caught before it became a bigger one.**
One ultrasonic sensor was briefly wired backwards (power and ground reversed) and started heating up. We caught it, disconnected it immediately, and rewired it correctly; it has worked since. This is exactly why we treat "every ground wire shares one common rail" as a hard rule everywhere else in this README — it's not caution for caution's sake, it's a lesson from something that actually almost went wrong.

### The pattern across all three

In every case, the fix was to reduce complexity and isolate one failure at a time: fewer sensors on a shared bus instead of debugging a flaky multiplexer, ultrasonic wall sensing instead of relying on infrared reflection, and replacement of the failed IMX219 setup with a working Arducam IMX708 camera.
