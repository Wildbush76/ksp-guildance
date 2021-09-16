import krpc
import math
connect = krpc.connect()

vessel = connect.space_center.active_vessel

#vessel.control.activate_next_stage()
vessel.control.throttle = 0.65;
vessel.control.sas = True
vessel.control.rcs = True
vessel.control.activate_next_stage()
while True:
    #print(vessel.control.yaw)
    alt = math.floor(vessel.flight().mean_altitude)
    if(alt > 1000 and alt < 10000):
        vessel.control.yaw = (alt - 1000)/75;
        #print("turning")
    elif(alt > 10000):
        vessel.control.yaw = 0
    if(alt > 30000):
        vessel.control.throttle = 1;
        
