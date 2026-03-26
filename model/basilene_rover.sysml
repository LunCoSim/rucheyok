/**
 * Basilene: 2kg Nano-Rover (v0.1)
 * ────────────────────────────────────
 * Derived from ClassC_NanoSwarmRover, reconfigured for
 * skid-steer mobility and 0.5U profile.
 *
 * Version:   0.1.0
 * Date:      2026-03-26
 */
package Basilene_Design {

    import LORS_RoverClasses::*;
    import LORS_Types::*;
    import LORS_Interfaces::*;

    /**
     * Basilene Nano-Rover
     * 2kg, 4-wheel skid-steer, 0.5U height.
     */
    part def Basilene_NanoRover :> ClassC_NanoSwarmRover {

        // ── Physical Envelope ──
        attribute width_mm : Real = 100.0;
        attribute length_mm : Real = 200.0;
        attribute height_mm : Real = 50.0;

        // ── Component Mass Budgeting (g) ──
        part chassis { attribute mass_g : Real = 500.0; }
        part motor_system { attribute mass_g : Real = 150.0; } // Motor + Gear/Belt box (2 sets)
        part wheels { attribute mass_g : Real = 300.0; } // 4 wheels
        part battery { attribute mass_g : Real = 300.0; }
        part control_unit { attribute mass_g : Real = 100.0; }
        part solar_panels { attribute mass_g : Real = 50.0; }
        part deployment_rails { attribute mass_g : Real = 300.0; }
        part misc { attribute mass_g : Real = 150.0; }

        // ── Total Calculated Mass (kg) ──
        attribute total_system_mass_kg : Real = (chassis.mass_g + 
                                               motor_system.mass_g + 
                                               wheels.mass_g + 
                                               battery.mass_g + 
                                               control_unit.mass_g + 
                                               solar_panels.mass_g + 
                                               deployment_rails.mass_g + 
                                               misc.mass_g) / 1000.0;

        // ── Mobility Reconfiguration (Skid-Steer) ──
        redefines mobility {
            :>> locomotion_type      = LocomotionType::Wheeled;
            :>> wheel_count          = 4;
            :>> suspension_type      = "Fixed"; // Rigid chassis
        }

        // ── Drive System ──
        part drive_train {
            attribute motor_count : Integer = 2;
            attribute drive_type : String = "Skid-Steer";
        }

        // ── Power System ──
        redefines eps {
            :>> battery_capacity_Wh = 40.0; // Increased for RPi
        }

        // ── Control / Data ──
        part control_unit {
            attribute processor : String = "Raspberry Pi Zero 2W";
        }
    }
}
