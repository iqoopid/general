import RPi.GPIO as GPIO
import time

RelayIn1 = 15
pin2 = 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RelayIn1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)

GPIO.output(RelayIn1, GPIO.LOW)

try:
    while True:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(RelayIn1, GPIO.OUT)
        GPIO.setup(pin2, GPIO.OUT)
        GPIO.output(RelayIn1, GPIO.LOW)
        switch1 = GPIO.input(pin2)
        print("Input: ", switch1)
        if switch1 == 1:
            print(GPIO.HIGH, switch1)
            GPIO.output(RelayIn1, GPIO.HIGH)
            time.sleep(5)
            GPIO.output(RelayIn1, GPIO.LOW)
            time.sleep(1)
            GPIO.cleanup()

        else:
            print("Inside else: ",GPIO.LOW, switch1)
            GPIO.output(RelayIn1, GPIO.LOW)
            GPIO.cleanup()
            time.sleep(1)
        


except KeyboardInterrupt:
    print("Stopped by User")
    GPIO.cleanup()


