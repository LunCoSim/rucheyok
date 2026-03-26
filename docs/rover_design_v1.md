# Design: 2U (100mm x 200mm) x 50mm Nano-Rover

## Overview
A 2 kg Nano-Rover based on the `ClassC_NanoSwarmRover` specification, utilizing a 0.5U height chassis for a low center of gravity.

## Design Constraints
- **Envelope:** 100mm x 200mm x 50mm (Total volume: 1L)
- **Mass Goal:** 2 kg (Total system: Rover + Deployer)
- **Mobility:** Skid-steer (2 motors, 4 wheels)

## Core Components
- **Chassis:** 6061-T6 Aluminum or Carbon Fiber composite frame.
- **Control Unit:** Raspberry Pi (Compute Module or Zero 2W) for GNC and mesh communication.
- **Power System (EPS):** Lithium-ion/polymer pouch cells (~20-50 Wh), integrated BMS, and localized solar charging (top surface).
- **Drive Train:**
    - 2 x DC Gear-motors (Left side, Right side).
    - Gear reduction for torque distribution.
    - 4 x Low-profile wheels.
- **Deployment:** Standardized rail system on sides for `DeploymentRailPort` compatibility.

## Physical Dimensions & Component Allocation

### Mass Budgeting (Total Goal: 2.0 kg)

| Component | Estimated Mass (g) | Qty | Subtotal (g) |
| :--- | :--- | :--- | :--- |
| **Main Chassis** | 500 | 1 | 500 |
| **Drive Motors** | 100 | 2 | 200 |
| **Gear/Belt Box** | 50 | 2 | 100 |
| **Wheels** | 75 | 4 | 300 |
| **Battery (LiPo)** | 300 | 1 | 300 |
| **Control (Pi+Carrier)**| 100 | 1 | 100 |
| **Solar Panels** | 50 | 1 | 50 |
| **Deployment Rails** | 300 | 1 | 300 |
| **Misc/Fasteners** | 150 | 1 | 150 |
| **TOTAL** | | | **2000** |

### Component Allocation (Top-Down View)
- **Forward (0-60mm):** Sensors/Camera, Deployment Interface.
- **Center (60-140mm):** Battery pack, RPi, EPS board (stacked).
- **Aft (140-200mm):** Motor drivers, redundant comms, power distribution.
- **Side (100mm span):** Drive train assembly (motors/gears), wheels.

