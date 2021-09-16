import krpc
import math

conn = krpc.connect()
rocket = conn.connect.space_center.active_vessel;

#abort
def abort(): 
  print("sucks to suck")
rocket.control.throttle = 0.7
while True:
  alt = math.floor(rocket.flight().mean_altitude)
  speed = math.floor(rocket.flight().velocity)
  gf = math.floor(rocket.flight().g_force)
