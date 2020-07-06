import time
import max7219

from machine import Pin, SPI
spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Matrix8x8(spi, Pin(15), 1)
display.brightness(0)
display.fill(0)
display.text('A',0,0,1)
display.show()
time.sleep(1)

display.fill(0)
display.show()
time.sleep(1)

display.pixel(0,0,1)
display.pixel(1,1,1)
display.hline(0,4,8,1)
display.vline(4,0,8,1)
display.line(8, 0, 16, 8, 1)
display.rect(17,1,6,6,1)
display.fill_rect(25,1,6,6,1)
display.show()
time.sleep(1)

display.fill(0)
display.text('d',0,0,1)
display.show()
time.sleep(1)

display.fill(0)
display.text('1',0,0,1)
display.show()
time.sleep(1)