import RPi.GPIO as GPIO
import time



def pump(Motor_Relay2, Switch2):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)          # GPIO Numbering
    GPIO.setup(Motor_Relay2,GPIO.OUT) # milk Pump
    GPIO.setup(Switch2,GPIO.OUT)
    GPIO.output(Motor_Relay2, GPIO.LOW) # Initially switch relay pin OFF. 
    switch = GPIO.input(Switch2)
    print("Input: ", switch)
    if switch == 1:
        print(GPIO.HIGH, switch)
        GPIO.output(Motor_Relay2, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(Motor_Relay2, GPIO.LOW)
    else:
        print(GPIO.LOW, switch)
        GPIO.output(Motor_Relay2, GPIO.LOW)
        time.sleep(2)