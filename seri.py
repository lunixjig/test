import serial

ser = serial.Serial(port = "/dev/ttyAMA0",
baudrate = 9600,
parity = serial.PARITY_NONE,
stopbits= serial.STOPBITS_ONE,
rtscts = False, dsrdtr = False)
print ser.portstr
ser.write("*AD-M2M4,RD:001#")
print ser.read()
ser.close()
