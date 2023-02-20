import threading
import RPi.GPIO as GPIO
from time import sleep

Switch = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)     # GPIO Numbering
GPIO.setup(Switch,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def intake():
    inpu = GPIO.input(Switch)
    if inpu == 1:
        t2 = threading.Thread(target=out, args=(inpu,))
        # starting thread 2
        t2.start()
        # wait until thread 2 is completely executed
        t2.join()
    else:
        print("False Condition", inpu)
    sleep(1)

def out(inpu):
    print("This is a Test output ", inpu)

if __name__ == '__main__':     # Program start from here
    try:
        while True:
            t1 = threading.Thread(target=intake)
            # starting thread 1
            t1.start()

            # wait until thread 1 is completely executed
            t1.join()
            
    except KeyboardInterrupt:
        print("Exit by user")
