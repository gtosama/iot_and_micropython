import machine
import time

led = machine.Pin(32 , machine.Pin.PULL_UP)
for i in range(1,6):
    led.value(1)
    time.sleep(1)
    led.value(0)
    time.sleep(1)
