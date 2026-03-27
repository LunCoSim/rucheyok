# 🛰️ Basilene Rover: Baseline Specification (v0.1)

## 1. Project Overview
**Basilene** is a 2kg lunar micro-rover designed for full compliance with the **Lunar Open-source Rover Standard (LORS)**. It features a 2U footprint and is optimized for modularity, low-cost assembly, and robust lunar surface mobility.

---

## 2. Technical Specifications
### 📐 Physical Dimensions
- **Chassis Envelope:** 200 mm (L) x 100 mm (W) x 50 mm (H)
- **Overall Stance:** 170 mm (W) wheel-to-wheel | 140 mm (H) ground-to-top
- **Ground Clearance:** 45 mm (nominal at chassis floor)

### 🏎️ Mobility & Drive
- **Drive Mode:** 4-wheel independent skid-steer
- **Wheels:** 4 x 140 mm diameter (70 mm radius) x 20 mm width
- **Wheelbase:** 170 mm
- **Drive Train:** Two independent internal DC gear-motors (Zone C) coupled with gearbox housings that drive front and rear axles per side.
- **Axles:** 3mm Stainless Steel stub axles.

### ⚖️ Mass Budget (Target: 2.0 kg)
| Component Group | Estimated Mass (g) | Notes |
| :--- | :--- | :--- |
| **Chassis Plates (5 total)** | 450 | Aluminum 6061-T6 (1.5mm) |
| **Drive Motors & Gearboxes** | 150 | High-torque DC micro gear-motors |
| **Wheels (4x)** | 350 | Lightweight honeycomb or hollow spoke |
| **Battery (LiPo)** | 400 | High-density 2S/3S pouch cells |
| **Avionics (Pi Zero + HAT)** | 100 | Main computer and motor controller |
| **Lid + Solar Panel** | 120 | 160x70mm solar integration |
| **Misc (Sensors, Cables)** | 30 | Wiring harness and camera |
| **TOTAL MASS** | **1600** | **~400g margin remaining for payload** |

---

## 3. Structural Breakdown
The monocoque chassis is assembled from aluminum 6061-T6 plates:
- **Base Plate** (`Plate_Base`): 200 x 100 mm foundation.
- **Side Plates (x2)**: Carry motor mounts and 180mm red deployment rails.
- **Front Plate**: Featuring a 12mm aperture for the fish-eye camera.
- **Rear Plate**: Interface for communications and power toggle.
- **Top Lid**: Solid lid with a 160 x 70 mm cutout for solar cell arrays.

---

## 4. Internal Packaging (Zone Mapping)
The internal volume is divided into three functional zones (X-axis measured from front):

| Zone | Range (X) | Components | Color |
| :--- | :--- | :--- | :--- |
| **Zone A (Fwd)** | 0–40 mm | Camera module, Sensor PCB, Bus System | 🟡 Yellow |
| **Zone B (Center)** | 40–140 mm | Raspberry Pi Zero 2W, EPS Stack, 80x40x12 Battery | 🟢 Green |
| **Zone C (Aft)** | 140–200 mm | DC Gear-Motors, Motor Driver PCBs, Comms | 🟠 / 🟣 |

### Critical Coordinates (Origin: Front-Bottom-Left)
- **Front Axles:** X = 15, Z = 25
- **Rear Axles:** X = 185, Z = 25
- **Camera Lens:** X = 200, Y = 50, Z = 35.5
- **Solar Cutout:** 20 to 180 on X, -35 to 35 on Y center.

---

## 5. System Electronics
- **Main Computer:** Raspberry Pi Zero 2W.
- **Vision:** 180° fish-eye camera module.
- **Power:** 2S/3S LiPo battery with integrated EPS.
- **Locomotion Control:** Dual-channel motor driver board (L298N or equivalent).
- **Telemetry:** Internal Mesh Wi-Fi module in Zone C.

---

## 6. Manufacturing & Assembly
1.  **Chassis Plates:** CNC or Laser-cut 6061-T6 Aluminum (1.5mm).
2.  **Fastening:** M2.5 stainless steel screws with internal L-brackets or PEM nuts.
3.  **Drive Train:** Motor shafts couple to internal gear/belt alleys; axles press-fit into side wall bearings.
4.  **Ingress Protection:** Silicone gaskets at plate edges for lunar dust mitigation.

---

## 🚀 Model Reproduction
The design is fully parametric. Use the following script in FreeCAD to generate the 3D model:
`model/basilene_rover_gen.py`

*Developed under the MoonDAO LORS initiative.*
