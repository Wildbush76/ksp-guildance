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
    rocket.control.parachutes = True
    phase =  4


print("rocket is ready for launch")
print("starting launch sequence")
rocket.control.throttle = 0.7
rocket.control.activate_next_stage()
print("lift off")

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

        
    
    
