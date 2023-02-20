#!/usr/bin/env python
import os

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
    print("\n"+text+"\n")
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def loop_temp(ds18b20):
    while True:
        if read_temp(ds18b20) != None:
            print("Current temperature : %0.3f C" % read_temp(ds18b20)[0])
            print("Current temperature : %0.3f F" % read_temp(ds18b20)[1])

def kill_temp():
    quit()

if __name__ == '__main__':
    try:
        serialNum = sensor_temp()
        loop_temp(serialNum)
    except KeyboardInterrupt:
        kill_temp()
    except IndexError:
        kill_temp()