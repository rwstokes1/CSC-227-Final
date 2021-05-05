import random
import time
from drone import Drone

my_drone = Drone()

x = 0

while x < 25:
    i = random.randint(1,4)
    if i == 1:
        my_drone.accelerate()
    elif i == 2:
        my_drone.decelerate()
    elif i == 3:
        my_drone.ascend()
    elif i == 4:
        my_drone.descend()
    my_drone.__str__()
    x += 1
    time.sleep(0.5)

print("Drone is beginning landing procedure...")
time.sleep(3)

speed = my_drone.getSpeed()
height = my_drone.getHeight()

while speed != 0 or height != 0:
    if speed < 0:
        my_drone.accelerate()
    elif speed > 0:
        my_drone.decelerate()
    elif height > 0:
        my_drone.descend()
    speed = my_drone.getSpeed()
    height = my_drone.getHeight()
    my_drone.__str__()
    time.sleep(1)

print("Flight has concluded\n")
