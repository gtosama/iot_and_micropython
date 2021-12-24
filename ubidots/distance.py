from hcsr04 import HCSR04
from machine import Pin


sensor = HCSR04(trigger_pin=32, echo_pin=33)

distance = sensor.distance_cm()

print('Distance:', distance, 'cm')

