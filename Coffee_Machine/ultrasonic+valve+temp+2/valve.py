import RPi.GPIO as GPIO
import time


def relay_switcher(Relay1_Ln1, Relay2_Ln2, Button1, Button2):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.setup(Relay1_Ln1, GPIO.OUT)
    GPIO.setup(Relay2_Ln2, GPIO.OUT)
    GPIO.setup(Button1, GPIO.IN)
    GPIO.setup(Button2, GPIO.OUT)
    GPIO.output(Relay1_Ln1, GPIO.LOW) # Initially switch relay pin OFF. 
    GPIO.output(Relay2_Ln2, GPIO.LOW) # Initially switch relay pin OFF. 

    switch1 = GPIO.input(Button1)
    switch2 = GPIO.input(Button2)
    print("Input: switch1: ", switch1)
    print("Input: switch2: ", switch2)    
    if switch1 == 1:
        print("if:")
        print("Button1: ", switch1)
        print("Button2: ", switch2)
        GPIO.output(Relay1_Ln1, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(Relay1_Ln1, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
    elif switch2 == 1:
        print("elif:")
        print("Button1: ", switch1)
        print("Button2: ", switch2)
        GPIO.output(Relay2_Ln2, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(Relay2_Ln2, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
    else:
        print("else:")
        print("Button1: ", switch1)
        print("Button2: ", switch2)
        GPIO.output(Relay1_Ln1, GPIO.LOW)
        GPIO.output(Relay2_Ln2, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
    
if __name__ == '__main__':     # Program start from here

    while True:
        relay_switcher(Relay1_Ln1= 26, Relay2_Ln2= 28, Button1= 13, Button2=21)