import machine
import utime

led = machine.Pin(4 , machine.Pin.PULL_DOWN)

while True:
    print(led.value())
    utime.sleep(1)