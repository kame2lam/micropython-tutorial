import max7219
from machine import Pin, SPI
spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
display = max7219.Matrix8x8(spi, Pin(15), 1)
display.brightness(0)
display.fill(0)
display.text('A',0,0,1)
display.show()