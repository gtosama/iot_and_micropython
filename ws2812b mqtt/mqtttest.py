import ubinascii
import machine
from umqtt.robust import MQTTClient


led=machine.Pin(33 , machine.Pin.PULL_UP)
 
def sub_cb(topic, msg):
    global led
    print((str(topic), str(msg)))
    if msg == b'led on':
        led.value(1)
    if msg == b'led off':
        led.value(0)
    
def connect_and_subscribe(mqtt_server, topic_sub):
  client_id = ubinascii.hexlify(machine.unique_id())
  client = MQTTClient(client_id, mqtt_server)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client
  
#mqtt_response('192.168.1.5','testTopic','hello from esp32')

try:
  client = connect_and_subscribe('broker.emqx.io' , 'testTopic')
except OSError as e:
  print('connect pb')
while True:
    try:
       client.check_msg()
    except OSError as e:
        print('houston we got a pb')