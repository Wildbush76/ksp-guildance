import krpc
import math

conn = krpc.connect()
rocket = conn.connect.space_center.active_vessel;

#abort
def abort(): 
  print("sucks to suck")
  
#controls and stuff

hover = False
prev  = 0;
rocket.control.throttle = 0.7
rocket.control.activate_next_stage()
while True:
  alt = math.floor(rocket.flight().mean_altitude)
  speed = math.floor(rocket.flight().velocity)
  gf = math.floor(rocket.flight().g_force)
  if(hover == True):
    if(speed > 4 and prev < alt):
      rocket.control.throttle -=0.1;
     elif(speed > 4 and prev > alt):
      rocket.control.throttle +=0.1;
      #make it do the funky hover
    #something
   else:
    if(speed > 250):
      rocket.control.throttle -= 0.1
    elif(speed < 200):
      rocket.control.throttle += 0.1
    if(alt > 5000):
      prev = alt
      hover = True
