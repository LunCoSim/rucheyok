import FreeCAD as App
import Part

def create_basilene_rover():
    # Clean slate
    doc_name = "Basilene_Final_Rover"
    try:
        App.closeDocument(doc_name)
    except:
        pass

    doc = App.newDocument(doc_name)

    # ══════════════════════════════════════════════════════
    # CONSTANTS (mm)
    # ══════════════════════════════════════════════════════
    CL = 200.0   # Chassis Length (X)
    CW = 100.0   # Chassis Width (Y)
    CH = 50.0    # Chassis Height (Z)
    W  = 1.5     # Wall thickness

    WR = 70.0    # Wheel radius
    WW = 20.0    # Wheel width
    WO = 3.0     # Wheel offset from chassis wall
    AZ = 25.0    # Axle height (Z)
    AXF = 15.0   # Front axle X
    AXR = 185.0  # Rear axle X

    MOT_R = 12.0   
    MOT_L = 30.0   

    # Colors
    gray = (0.75, 0.75, 0.75)
    wheel_col = (0.8, 0.6, 0.25) # Metallic bronze/gold for contrast

    # ══════════════════════════════════════════════════════
    # HELPERS
    # ══════════════════════════════════════════════════════
    def ycyl(name, r, h, cx, cy, cz, col=(0.5,0.5,0.5)):
        c = doc.addObject("Part::Cylinder", name)
        c.Radius = r; c.Height = h
        c.Placement.Base = App.Vector(cx, cy - h/2.0, cz)
        c.Placement.Rotation = App.Rotation(App.Vector(1,0,0), -90)
        c.ViewObject.ShapeColor = col
        return c

    # ══════════════════════════════════════════════════════
    # 1. CHASSIS — 5 separate plates
    # ══════════════════════════════════════════════════════
    base = doc.addObject("Part::Box", "Plate_Base")
    base.Length, base.Width, base.Height = CL, CW, W
    base.Placement.Base = App.Vector(0, -CW/2, 0)
    base.ViewObject.ShapeColor = gray

    side_l = doc.addObject("Part::Box", "Plate_Side_L")
    side_l.Length, side_l.Width, side_l.Height = CL, W, CH
    side_l.Placement.Base = App.Vector(0, -CW/2 - W, 0)
    side_l.ViewObject.ShapeColor = gray

    side_r = doc.addObject("Part::Box", "Plate_Side_R")
    side_r.Length, side_r.Width, side_r.Height = CL, W, CH
    side_r.Placement.Base = App.Vector(0, CW/2, 0)
    side_r.ViewObject.ShapeColor = gray

    front_s = doc.addObject("Part::Box", "Front_Solid")
    front_s.Length, front_s.Width, front_s.Height = W, CW, CH
    front_s.Placement.Base = App.Vector(CL, -CW/2, 0)
    cam_hole = doc.addObject("Part::Cylinder", "CamHole")
    cam_hole.Radius = 6; cam_hole.Height = W + 2
    cam_hole.Placement.Base = App.Vector(CL - 1, 0, W + 10.5)
    cam_hole.Placement.Rotation = App.Rotation(App.Vector(0,1,0), 90)
    front_p = doc.addObject("Part::Cut", "Plate_Front")
    front_p.Base = front_s; front_p.Tool = cam_hole
    front_p.ViewObject.ShapeColor = gray
    front_s.ViewObject.Visibility = False
    cam_hole.ViewObject.Visibility = False

    rear = doc.addObject("Part::Box", "Plate_Rear")
    rear.Length, rear.Width, rear.Height = W, CW, CH
    rear.Placement.Base = App.Vector(-W, -CW/2, 0)
    rear.ViewObject.ShapeColor = gray

    # ══════════════════════════════════════════════════════
    # 2. LID
    # ══════════════════════════════════════════════════════
    lid_s = doc.addObject("Part::Box", "Lid_Solid")
    lid_s.Length, lid_s.Width, lid_s.Height = CL, CW, W
    lid_s.Placement.Base = App.Vector(0, -CW/2, CH)
    solar_cut = doc.addObject("Part::Box", "SolarCut")
    solar_cut.Length, solar_cut.Width, solar_cut.Height = 160, 70, W + 2
    solar_cut.Placement.Base = App.Vector(20, -35, CH - 1)
    lid = doc.addObject("Part::Cut", "Plate_Lid")
    lid.Base = lid_s; lid.Tool = solar_cut
    lid.ViewObject.ShapeColor = (0.8, 0.8, 0.85)
    lid.ViewObject.Transparency = 0
    lid_s.ViewObject.Visibility = False
    solar_cut.ViewObject.Visibility = False

    # ══════════════════════════════════════════════════════
    # 3. WHEELS (Updated Color)
    # ══════════════════════════════════════════════════════
    WCY = CW/2.0 + W + WO + WW/2.0  

    for name, x, y in [("Wheel_FL", AXF, -WCY), ("Wheel_FR", AXF, WCY),
                        ("Wheel_RL", AXR, -WCY), ("Wheel_RR", AXR, WCY)]:
        ycyl(name, WR, WW, x, y, AZ, wheel_col)

    # ══════════════════════════════════════════════════════
    # 4. STUB AXLES
    # ══════════════════════════════════════════════════════
    stub_len = W + WO + WW/2.0  
    shaft_col = (0.55, 0.55, 0.55)

    for name, ax_x, side in [("Stub_FL", AXF, -1), ("Stub_FR", AXF, 1),
                               ("Stub_RL", AXR, -1), ("Stub_RR", AXR, 1)]:
        stub_cy = side * (CW/2.0 + stub_len/2.0)
        ycyl(name, 4, stub_len, ax_x, stub_cy, AZ, shaft_col)

    # ══════════════════════════════════════════════════════
    # 5. INTERNAL DRIVE TRAIN
    # ══════════════════════════════════════════════════════
    gb_len = AXR - AXF + 16 
    gb_width = 16
    gb_height = 16

    gbl = doc.addObject("Part::Box", "Gearbox_L")
    gbl.Length, gbl.Width, gbl.Height = gb_len, gb_width, gb_height
    gbl.Placement.Base = App.Vector(AXF - 8, -CW/2.0, AZ - gb_height/2.0)
    gbl.ViewObject.ShapeColor = (0.3, 0.3, 0.35)

    gbr = doc.addObject("Part::Box", "Gearbox_R")
    gbr.Length, gbr.Width, gbr.Height = gb_len, gb_width, gb_height
    gbr.Placement.Base = App.Vector(AXF - 8, CW/2.0 - gb_width, AZ - gb_height/2.0)
    gbr.ViewObject.ShapeColor = (0.3, 0.3, 0.35)

    MOTOR_X = 140.0
    motor_l_body_cy = -CW/2.0 + gb_width + MOT_R
    ycyl("Motor_L_Body", MOT_R, MOT_L, MOTOR_X, motor_l_body_cy, AZ, (0.4, 0.15, 0.15))

    motor_r_body_cy = CW/2.0 - gb_width - MOT_R
    ycyl("Motor_R_Body", MOT_R, MOT_L, MOTOR_X, motor_r_body_cy, AZ, (0.4, 0.15, 0.15))

    # ══════════════════════════════════════════════════════
    # 6. EXTERNAL DEPLOYMENT RAILS
    # ══════════════════════════════════════════════════════
    for side, yp in [("Rail_L", -CW/2 - W - 2), ("Rail_R", CW/2 + W)]:
        r = doc.addObject("Part::Box", side)
        r.Length, r.Width, r.Height = 180, 2, 5
        r.Placement.Base = App.Vector(10, yp, 12)
        r.ViewObject.ShapeColor = (0.8, 0.1, 0.1)

    # ══════════════════════════════════════════════════════
    # 7. ZONE A : Sensors & Camera
    # ══════════════════════════════════════════════════════
    cam = doc.addObject("Part::Box", "Camera")
    cam.Length, cam.Width, cam.Height = 15, 15, 15
    cam.Placement.Base = App.Vector(CL - 15, -7.5, W + 3)
    cam.ViewObject.ShapeColor = (0.95, 0.85, 0.1)

    lens = doc.addObject("Part::Cylinder", "Lens")
    lens.Radius = 5; lens.Height = 6
    lens.Placement.Base = App.Vector(CL - 2, 0, W + 10.5)
    lens.Placement.Rotation = App.Rotation(App.Vector(0,1,0), 90)
    lens.ViewObject.ShapeColor = (0.1, 0.1, 0.2)

    sens = doc.addObject("Part::Box", "Sensor_PCB")
    sens.Length, sens.Width, sens.Height = 35, 50, 2
    sens.Placement.Base = App.Vector(CL - 38, -25, W + 25)
    sens.ViewObject.ShapeColor = (0.85, 0.85, 0.2)

    # ══════════════════════════════════════════════════════
    # 8. ZONE B + C : Electronics
    # ══════════════════════════════════════════════════════
    bat = doc.addObject("Part::Box", "Battery")
    bat.Length, bat.Width, bat.Height = 80, 40, 12 
    bat.Placement.Base = App.Vector(50, -20, W)
    bat.ViewObject.ShapeColor = (0.25, 0.25, 0.85)

    pz = W + 12 + 8
    pi = doc.addObject("Part::Box", "Pi_Zero")
    pi.Length, pi.Width, pi.Height = 65, 30, 2
    pi.Placement.Base = App.Vector(58, -15, pz)
    pi.ViewObject.ShapeColor = (0.1, 0.65, 0.1)

    for sx, sy in [(60, -13), (60, 13), (121, -13), (121, 13)]:
        s = doc.addObject("Part::Cylinder", f"Post_{sx}_{sy}")
        s.Radius = 1.5; s.Height = 8
        s.Placement.Base = App.Vector(sx, sy, W + 12)
        s.ViewObject.ShapeColor = (0.7, 0.7, 0.0)

    mdl = doc.addObject("Part::Box", "MotorDrv_L")
    mdl.Length, mdl.Width, mdl.Height = 25, 20, 3
    mdl.Placement.Base = App.Vector(20, -30, W + 5)
    mdl.ViewObject.ShapeColor = (0.95, 0.5, 0.1)

    mdr = doc.addObject("Part::Box", "MotorDrv_R")
    mdr.Length, mdr.Width, mdr.Height = 25, 20, 3
    mdr.Placement.Base = App.Vector(20, 10, W + 5)
    mdr.ViewObject.ShapeColor = (0.95, 0.5, 0.1)

    com = doc.addObject("Part::Box", "Comms")
    com.Length, com.Width, com.Height = 25, 20, 10
    com.Placement.Base = App.Vector(10, -10, W + 15)
    com.ViewObject.ShapeColor = (0.55, 0.2, 0.6)

    doc.recompute()
    return doc

if __name__ == "__main__":
    create_basilene_rover()
