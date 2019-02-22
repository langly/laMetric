## 8x8 display for RGB stuff...
from binascii import hexlify
from struct import pack
from time import sleep
from math import sin
from draw import *

height = 8
width  = 38

clear()

offset = 0
while(1):
	clear()
	for x in range(1,width):
		s = (sin(x+offset) + 1.0) / 2.0
		sprev = (sin(x+offset-1) + 1.0) / 2.0
		y = int(s * height)
		yprev = int(sprev * height)
		drawLine(x-1,yprev , x, y, 0xFFFF)

	offset = offset+1
	sleep(.1)
