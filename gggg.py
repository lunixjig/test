import smbus
import time

bus = smbus.SMBus(1)

DE = 0x20
OUT = 0x00
IN = 0x01

GPA = 0x12
GPB = 0x13

bus.write_byte_data(DE,OUT,0xFF)
bus.write_byte_data(DE,IN,0x00)

a = 0
while True:
	a = 0xff - bus.read_byte_data(DE,GPA)
	b = 0
	for x in range(8):
		b = b * 2
		b = b + ((a >> x) % 2)	
	bus.write_byte_data(DE,GPB,b)
