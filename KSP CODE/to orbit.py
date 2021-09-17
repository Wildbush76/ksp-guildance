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
    #oh shit something went wrong
    rocket.control.abort = True
    time.sleep(6)
    rocket.control.sas = False
    rocket.control.parachutes = True
    phase =  4

rocket.control.throttle = 0.7
rocket.control.activate_next_stage()

while(phase != 4):
    altitude = rocket.flight().mean_altitude
    heading = rocket.flight().heading
    if(rocket.flight().pitch < -1):
        abort()
    if(phase == 1):
        targetPitch = 90 * ((50000 - altitude) / 50000)
        pitchDiff = rocket.flight().pitch - targetPitch
        if(rocket.thrust == 0.0):
            rocket.control.activate_next_stage()
        if (heading < 180 and altitude < 50000):
            rocket.control.yaw = (pitchDiff / 90)
        elif(altitude < 50000): 
            rocket.control.yaw = 0.5
        if(rocket.orbit.apoapsis  > 100000):
            phase = 2#enter phase two
            rocket.control.sas = True
            rocket.control.rcs = True
            sleep(0.5)
            rocket.control.sas_mode = conn.space_center.SASMode.prograde
            Print("Entering cruise stage")
    elif(phase == 2):
        if(altitude > 90000):
            phase 
        

        
    
    
