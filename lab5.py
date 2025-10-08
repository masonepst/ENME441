import RPi.GPIO as GPIO
import time
import math

GPIO.setmode(GPIO.BCM)
timer = time.time()
LED = [2,3,4,17,27,22,14,15,18,23]
f = 0.2

LED_pwm = []

def on():
	n = 1

def off():
	n = -1

GPIO.add_event_detect(21, gpio.RISING, callback = on, bouncetime = 100)
GPIO.add_event_detect(21, gpio.FALLING, callback = off, bouncetime = 100)

for i in range(len(LED)):
	GPIO.setup(LED[i], GPIO.OUT)
	pwm = GPIO.PWM(LED[i],500)
	pwm.start(0)
	LED_pwm.append(pwm)

while True:
		t = time.time() - timer
		for i in range(len(LED_pwm)):
			B = math.sin(2*math.pi*f*t-i*n*math.pi/11)
			B = B**2
			brightness = B*100
			LED_pwm[i].ChangeDutyCycle(brightness)

for i in range(len(LED_pwm)):
	LED_pwm[i].stop()
	GPIO.cleanup()

