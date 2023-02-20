import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
pin1 = 12
GPIO.setup(pin1, GPIO.OUT)

while True:
	GPIO.output(pin1, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(pin1, GPIO.LOW)
	time.sleep(1)
