from machine import Pin
import neopixel

np = neopixel.NeoPixel(Pin(32),7)

np[0] = (255,255,255)
np[1] = (255,0,0)
np[2] = (0,0,255)

np.write()
