import smbus
import time

bus = smbus.SMBus(1)

DE = 0x68

CHN = 0
CMB = 1
SRS = 0
PGA = 0

ch = (1 * 0x80) + (CHN * 0x20) + (CMB * 0x10) + (SRS * 2) + PGA
bus.write_byte(DE,ch)
while True :
	time.sleep(1)
	data = bus.read_i2c_block_data(DE,0,2)

	raw_adc = (data[0] & 0x0F) * 256 + data[1]
 	if raw_adc > 2047 :
		raw_adc -= 4096

	print 'input : ',raw_adc
