import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs 
Motor1A = 2
Motor1B = 3
#Motor1E = 4
Switch = 14

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    #GPIO.setup(Motor1E,GPIO.OUT)
    GPIO.setup(Switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def run(Switch1):
    # Run Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    sleep(4.5)
    print("Running: ",Switch1)
    #sleep(1)

def stop(Switch1):
    # Stop Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    sleep(0.1)
    print("Stationary: ",Switch1)
    #sleep(1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        while True:
            Switch1 = GPIO.input(Switch)
            print("check: ", Switch1)
            if Switch1 == GPIO.HIGH:
                print("inside: ", GPIO.HIGH)
                run(Switch1)
            else:
                stop(Switch1)
    except KeyboardInterrupt:
        destroy()
