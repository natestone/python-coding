###USAGE###
# pip3 install makeblock --upgrade
###########
print('1')
from time import sleep
print('2')
from random import random
print('3')
import math
print('4')
#from makeblock import MegaPi
from megapi import * 
print('5')
A6 = 60
A7 = 61
A8 = 62
A9 = 63
A10= 64
A11= 65
A12= 66
A13= 67
A14= 68
A15= 69

print ("connecting")
bobMegapi = MegaPi()
print ("connecting")

#bobMegapi.start("/dev/cu.usbserial-1110") # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
bobMegapi.start("/dev/tty.usbserial-1110") # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
#bobMegapi.start("/dev/ttyUSB0") # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
# bobMegapi.start() # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
# bobMegapi = MegaPi.start("/dev/ttyAMA0") # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
#bobMegapi = MegaPi.start(SerialPort.connect("/dev/ttyUSB0")) # or megapi = MegaPi.connect(SerialPort.connect("/dev/ttyXXXX"))
print ("connected")
led = bobMegapi.RGBLed()
# bobMegapi.rgbLedSetColor(0,0,0,128,128,128)
print ("lights")
j = 0
f = 0
k = 0
pixels = [0]*12
print ("starting loop")
while(1):
  for t in range(0,4):
    pixels[t*3] = int(16 * (1 + math.sin(t / 2.0 + j / 4.0)))
    pixels[t*3+1] = int(16 * (1 + math.sin(t / 1.0 + f / 9.0 + 2.1)))
    pixels[t*3+2] = int(16 * (1 + math.sin(t / 3.0 + k / 14.0 + 4.2)))
  led.set_colors(pixels,A13)
  j += random()
  f += random()
  k += random()
  print (j + " - " + f + " - " + k)
  sleep(1.0)

