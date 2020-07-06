import time
from machine import Pin

BD1={'D4':2,
      'D3':0,
      'D2':4,
      'D1':5,
      'D0':16,
      'D5':14,
      'D6':12,
      'D7':13,
      'D8':15}

led=Pin(2,Pin.OUT)          #create LED object from pin2,Set Pin2 to output

while True:
  led.value(1)              #turn off
  time.sleep(0.5)
  led.value(0)              #turn on
  time.sleep(0.5)

      