# 8x8 display for RGB stuff...
from struct import pack
from time import sleep
from math import sin

### Two bytes per pixel
## 74 / 2 = 38 rows 
## Only the first 8 colums are RGB. Rest are greyscale

## Format is RGBb, where b is brightness
bytes_per_row 	= 74
bytes_per_pixel = 2

height = 8
width  = 38

def toggle():
	with open("/dev/fb0","w") as f:
		col = 0x0
		while 1:
			f.seek(0)
			for x in range(0, 8):
				## Square	
				for y in range(0,8):
					f.write(pack('H', col ))
				for y in range(0,29):
					f.write(pack('H', (1<<16)-1 ))

			f.flush()
			col = (col + 0x1110) % ( 1<<16 ) -1
			sleep(1)

def clear():
	with open("/dev/fb0","w") as f:
		for x in range(0,38*8):
			f.write(pack('H', 0 ))

def set(x,y,color):
	with open("/dev/fb0","w") as f:
		offset = y * bytes_per_row + ( bytes_per_pixel * x)
		f.seek(offset)
		f.write(pack('H',color))

def sign(r):
	if r >= 0: 
		return 1
	else :
		return -1

def drawLineLow(x0, y0, x1,y1, col):
	deltaX = float(x1 - x0)
	deltaY = float(y1 - y0)
	yi = 1
	deltaErr = abs(deltaY/deltaX)
	if deltaY < 0:
		yi = -1
		deltaY =-deltaY
	D = 2*deltaY - deltaX

	y = y0
	error = 0.0

	for x in range(x0, x1):
		error = error + deltaErr
		set(x,y,col)
		if ( error >= .5 ):
			y = min(y + sign(deltaY) * 1,0)
			error = error -1.0

def drawLineHigh(x0, y0, x1, y1,col):
	dx = x1 - x0
	dy = y1 - y0

	xi = 1
	
	if dx < 0:
		xi = -1
		dx = -dx
	D = 2*dx - dy
	x = x0

	for y in range(y0,y1):
		set(x,y, col)
		if D > 0:
			x = x + xi
			D = D - 2*dy

		D = D + 2*dx	

def drawLine(x0,y0, x1,y1, col):
	if abs(y1-y0) < abs(x1-x0):
		if ( x0 > x1 ):
			drawLineLow(x1,y1,x0,y0,col)
		else:
			drawLineLow(x0,y0,x1,y1,col)
	else: 
		if ( y0 > y1 ):
			drawLineHigh(x1,y1,x0,y0,col)
		else: 
			drawLineHigh(x0,y0,x1,y1,col)
