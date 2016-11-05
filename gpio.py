import RPi.GPIO as GPIO
import time

nv = 

GPIO.setmode(GPIO.BCM)

GPIO.setup(nv,GPIO.OUT)
GPIO.output(nv,False)

GPIO.output(nv,True)

time.sleep(1)
GPIO.output(nv,False)

GPIO.cleanup()
