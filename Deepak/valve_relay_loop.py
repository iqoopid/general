import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

Relay_Valve1 = 11
Relay_Valve2 = 12

GPIO.setup(Relay_Valve1,GPIO.OUT)
GPIO.output(Relay_Valve1, GPIO.LOW)
GPIO.output(Relay_Valve2, GPIO.LOW)



def start_relay():
    GPIO.output(Relay_Valve1, GPIO.HIGH)
    print("Relay0 ON")
    time.sleep(1)


def halt_relay():
    GPIO.output(Relay_Valve1, GPIO.LOW)
    print("Relay0 OFF")
    time.sleep(1)
    # GPIO.cleanup()

while True:
    start_relay()
    print("Relay ON")
    halt_relay()
    print("Relay OFF")