import RPi.GPIO as GPIO
from time import sleep


# Pins for Motor Driver Inputs 
Motor1A = 3
Motor1B = 5

def setup():
    print("Setup")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)


def run():
    # Run Motor
    print("Run Motor")
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    sleep(0.1)
    #sleep(1)
    


def stop():
    print("Stop Motor")
    # Stop Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    sleep(0.1)
    #sleep(1)


if __name__ == '__main__':
    try:
        while True:
            setup()
            sleep(1)
            run()
            sleep(3)
            stop()
            sleep(1)
 
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()