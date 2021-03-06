from umqtt.robust import MQTTClient

import machine as m
from hcsr04 import HCSR04
import ubinascii
import network
import time


sensor = HCSR04(trigger_pin=32, echo_pin=33)

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

ubidotsToken = "BBFF-kHa768viRSkOeRHPtTBliBV0CGM1GP" 

clientID = ubinascii.hexlify(m.unique_id())
print(ubinascii.hexlify(m.unique_id()))

client = MQTTClient("clientID", "industrial.api.ubidots.com", 1883,
                    user = ubidotsToken,
                    password = ubidotsToken)

def checkwifi():
    while not sta_if.isconnected():
        time.sleep_ms(500)
        print(".")
        sta_if.connect()

def publish():    
    while True:
        checkwifi()
        distance = sensor.distance_cm()
        client.connect()
        msg = b'{"distance": {"value":%s}}' % (distance)
        print("distance envoyée = ", distance)
        client.publish(b"/v1.6/devices/esp32-waterlvl", msg)        
        client.disconnect()
        time.sleep(10)

publish()