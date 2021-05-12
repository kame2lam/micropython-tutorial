# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()

import network

ssid='wf4'
password='12345678'


#STA_IF
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  print('connecting to network...')
  sta_if.active(True)
  sta_if.connect(ssid, password)
  while not sta_if.isconnected():
    pass
print('network config:', sta_if.ifconfig())


'''
#AP_IF
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=ssid, password=password)
while ap.active() == False:
  pass
print('Connection successful')
print(ap.ifconfig())
'''