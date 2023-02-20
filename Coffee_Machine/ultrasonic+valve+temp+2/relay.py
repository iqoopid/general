import RPi.GPIO as GPIO
import time


channel = 12

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(channel, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, GPIO.LOW)  # Turn relay off

def relay_off(pin):
    # Turn relay off when pin is setup to input mode:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("relay OFF")
    time.sleep(1)


def relay_on(pin):
    # Turn relay on by sending OFF value to pin (i.e., 0 Volts)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    print("relay ON")
    time.sleep(1)


if __name__ == '__main__':
    try:
        while True:
            relay_on(channel)
            relay_off(channel)
    except KeyboardInterrupt:
        GPIO.cleanup()