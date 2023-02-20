from threading import Thread
import RPi.GPIO as GPIO
import time


def distance_calc(Motor1A, Motor1B, GPIO_TRIGGER, GPIO_ECHO):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger to LOW after 0.01ms
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    print("Inside 'distance_calc()'")
    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        # print("StartTime:", StartTime)
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        # print("StopTime", StopTime)
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    print("distance: ", distance," cms")
    if distance >= 7:
        run(Motor1A, Motor1B, GPIO_ECHO)
    elif distance <= 7:
        stop(Motor1A, Motor1B, GPIO_ECHO)
    print("Measured Distance = %.1f cm" % distance)

def run(Motor1A, Motor1B, GPIO_ECHO):
    GPIO.setwarnings(False)
    # Run Motor
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    time.sleep(0.1)
    print("Running: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)
    
def stop(Motor1A, Motor1B, GPIO_ECHO):
    GPIO.setwarnings(False)
    # Stop Motor
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    time.sleep(0.1)
    print("Stationary: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)

if __name__ == '__main__':     # Program start from here
    Relay4_Pump = 6
    GPIO_TRIGGER = 18
    GPIO_ECHO = 24
    while True:
        dist = distance_calc(Relay4_Pump, GPIO_TRIGGER, GPIO_ECHO)
        time.sleep(0.5)