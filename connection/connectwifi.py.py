def do_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')

        #replace ssid and password with your ssid and pass
        wlan.connect('ssid', 'password')
        
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())  
    

do_connect()

import ntptime,utime
ntptime.settime()
t = utime.localtime()
print(t)