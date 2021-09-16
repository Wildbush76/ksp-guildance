import math
import krpc
connnect = krpc.connect()
rocket = connect.space_center.active_vessel

rocket.control.throttle = 1
rocket.control.sas = True
rocket.control.rcs = True
rocket.control.active_next_stage()

while True:
  alt = math.floor(rocket.flight().mean_altitude)
  speed = math.floor(rocket.flight().velocity)
  heading = math.floor(rocket.flight().heading)
  print(rocket.flight().heading)
  if(alt > 1000 and alt < 10000 and heading < 45):
    rocket.control.yaw = 2;
    #death is soon so well lets go
  elif(alt > 1000):
    rocket.control.yaw = 0
