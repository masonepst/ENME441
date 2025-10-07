# LED order 2,3,4,17,27,22,14,15,18,23

import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

pwm = GPIO.PWM(2,500)
pwm.start(0)
timer = time.time()
f = 0.2

while True:
	t = time.time() - timer
	B = math.sin(2*math.pi*f*t)
	B = B**2

	brightness = B*100

	pwm.ChangeDutyCycle(brightness)

pwm.stop()
GPIO.cleanup()

