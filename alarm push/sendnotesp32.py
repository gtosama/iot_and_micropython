def send_push_note(push,phone_id):    
    
    import ntptime,utime
    ntptime.settime()
    t = utime.localtime()
    
    data = {'type' : 'note' ,
            'body' : 'attention porte ouverte',
            'title': 'esp32 '+str(t[2])+'/'+str(t[1])+'/'+str(t[0]),
            'device_iden':phone_id} 

    push.make_push(phone_id , json.dumps(data))
    #push.send_sms("" , phone_id,"attention porte ouverte")


import machine
import utime

ala = machine.Pin(4 , machine.Pin.PULL_DOWN)

from pushbullet import Pushbullet
import json

Key = 'o.Nz63U4z2oyDSsFjwiIWknIaKyuJmugPT' 

push = Pushbullet(Key)
phone_id = push.get_device_id('HUAWEI HUAWEI VNS-L31')

#pour le sms
push.get_user_id()
    
while True:
    if ala.value() == 0:
        send_push_note(push,phone_id)
        utime.sleep(15)
    utime.sleep(1)

