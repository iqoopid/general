import os
import RPi.GPIO as GPIO
import time



def sensor_temp():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20


def read_temp(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    # print("\n"+text+"\n")
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit   


def kill_temp():
    quit()


def start_heater(Relay3_Heater):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.setup(Relay3_Heater, GPIO.OUT)
    GPIO.output(Relay3_Heater, GPIO.LOW) # Initially switch relay pin OFF.
    GPIO.output(Relay3_Heater, GPIO.LOW)
    GPIO.cleanup()


def halt_heater(Relay3_Heater):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)              # GPIO Numbering
    GPIO.setup(Relay3_Heater, GPIO.OUT)
    GPIO.output(Relay3_Heater, GPIO.LOW) # Initially switch relay pin OFF.
    GPIO.output(Relay3_Heater, GPIO.HIGH)


def temp_control(Relay3_Heater):
    serialNum = sensor_temp()
    celsius = read_temp(serialNum)[0]
    farenheit = read_temp(serialNum)[1]
    if read_temp(serialNum) != None:
        print("Current temperature : {0} C, {1} F".format(celsius, farenheit)) # Display temp in C, F
    if celsius >= 50.0:
        halt_heater(Relay3_Heater)
    elif celsius < 50.0:
        start_heater(Relay3_Heater)
    time.sleep(0.5)
     


if __name__ == '__main__':     # Program start from here
    while True:
        temp_control(Relay3_Heater=21)