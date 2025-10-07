# LED = [2,3,4,17,27,22,14,15,18,23]

import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)

pwm = GPIO.PWM(2,500)
pwm2 = GPIO.PWM(3,500)
pwm.start(0)
timer = time.time()
f = 0.2

while True:
	t = time.time() - timer
	# B = math.sin(2*math.pi*f*t)
	# B = B**2

	# brightness = B*100

	# pwm.ChangeDutyCycle(brightness)

	B2 = math.sin(2*math.pi*f*t-math.pi/11)
	B2 = B2**2
	brightness2 = B2*100
	pwm2.ChangeDutyCycle(brightness2)

pwm.stop()
pwm2.stop()
GPIO.cleanup()

