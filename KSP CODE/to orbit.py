import time
import krpc
import math
conn = krpc.connect()
rocket = conn.space_center.active_vessel
#rocket.control.sas = True
#rocket.control.rcs = True
phase = 1
#abort
def abort():
    print("ABORTING LAUNCH")
    rocket.control.abort = True
    time.sleep(6)
    rocket.control.sas = False
    rocket.control.rcs = False
    rocket.control.parachutes = True
    phase =  4

rocket.control.throttle = 0.7
rocket.control.activate_next_stage()

while(phase != 4):
    altitude = rocket.flight().mean_altitude
    heading = rocket.flight().heading
    speed = rocket.flight(rocket.orbit.body.reference_frame).speed
    #speed relative to kerbin i think ^
    if(rocket.flight().pitch < -1):
        abort()
    if(phase == 1):
        targetPitch = 90 * ((50000 - altitude) / 50000)
        pitchDiff = rocket.flight().pitch - targetPitch
        if(rocket.thrust == 0.0):
            rocket.control.activate_next_stage()
        if (heading < 180 and altitude < 50000):#gravity turn
            rocket.control.yaw = (pitchDiff / 90)
        elif(altitude < 50000): 
            rocket.control.yaw = 0.5
        if(rocket.orbit.apoapsis  > 100000):#MECO
            phase = 2#enter phase two
            rocket.control.sas = True
            rocket.control.rcs = True
            time.sleep(0.5)
            rocket.control.sas_mode = conn.space_center.SASMode.prograde
            Print("Entering cruise stage")
    elif(phase == 2):
        if(altitude > 90000):
            phase = 3#going for orbit
    elif(phase == 3):
        rocket.control.throttle = 1
        if(rocket.orbit.periapsis  > 70000):
            print("reached orbit")
            rocket.control.throttle = 0
            rocket.control.sas = False
            phase = 4
     elif(phase == 4):
        print("press enter to de-orbit")
        input()
        rocket.control.sas = True
        time.sleep(1)
        rocket.control.sas_mode = conn.space_center.SASMode.retrograde
        time.sleep(5)
        while(rocket.orbit.periapsis > 40000):
            rocket.throttle = 1
            if(rocket.thrust == 0.0):
                print("oh no")
                phase = 5
                break
        rocket.control.sas = False
        rocket.control.rcs = False
        rocket.control.parachutes = True
        rocket.control.activate_next_stage()
        

            
