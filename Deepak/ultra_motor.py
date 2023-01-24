import RPi.GPIO as GPIO
import time

# Pins for Motor Driver Inputs 
Motor1A = 3
Motor1B = 5
#set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18

GPIO.setwarnings(False)
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
GPIO.output(GPIO_TRIGGER, GPIO.LOW) 


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if distance >= 100:
        run(GPIO_ECHO)
    elif distance <= 50:
        stop(GPIO_ECHO)
    return distance

def run(GPIO_ECHO):
    # Run Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    time.sleep(0.1)
    print("Running: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)
    


def stop(GPIO_ECHO):
    # Stop Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    time.sleep(0.1)
    print("Stationary: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)


def destroy():
    GPIO.cleanup()


def main():
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        destroy()


if __name__ == '__main__':     # Program start from here
    main()
