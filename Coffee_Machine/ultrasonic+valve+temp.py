'''
UltraSonic Sensor VCC pin to Raspberry pi 5V pin
Ultra Trig pin to Pi GP18 pin
Ultra Echo pin to Pi GP24 pin
Ultra Gnd pin to Pi GND pin

Pi GP02 to Motor Driver Line1
GP03 to ln2

Motor Driver Out-1 to Motor cable
Out-2 to Motor cable
GND to Power Supply GND
+12V to Power Supply +9.5V

Pi GP05 to Switch1
5V to Switch1

Pi GP07 to Switch2
5V to Switch2

Pi GP15 to Relay ln1
Pi GP17 to Relay ln2
Pi GP08 to Relay ln3
5V to VCC
GND to GND

Relay1 NO to +ve of Valve1
Relay1 Common to +ve of 24V Power Supply

Valve1 -ve to GND of 24V Power

Relay2 NO to +ve of Valve2
Relay2 Common to +ve of 24V Power Supply

Valve2 -ve to GND of 24V Power 

Relay3 NO to +ve of Water Heater
Relay3 Common to +ve of 230V Power Supply

Water Heater -ve to GND of 230V Power 

'''
#!/usr/bin/env python
import os
import RPi.GPIO as GPIO
from time import sleep
import time


Motor1A = 2 # Pin1 for Motor Driver Inputs 
Motor1B = 3 # Pin2 for Motor Driver Inputs 
Motor_Relay2 = 8 # Relay for water Pump
Switch2 = 14
GPIO_TRIGGER = 18
GPIO_ECHO = 24
RelayIn1 = 15
RelayIn2 = 17
pin1 = 5
pin2 = 7
Heater_Relay3 = 9 # Relay for potable water heater


def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(Motor1A,GPIO.OUT)  # All pins as Outputs
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor_Relay2,GPIO.OUT) # water Pump
    GPIO.setup(Switch2,GPIO.OUT)
    GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
    GPIO.setup(GPIO_ECHO,GPIO.IN)
    GPIO.setup(RelayIn1, GPIO.OUT)
    GPIO.setup(RelayIn2, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(Heater_Relay3, GPIO.OUT)
    GPIO.output(RelayIn1, GPIO.LOW) # Initially switch relay pin OFF. 
    GPIO.output(RelayIn2, GPIO.LOW) # Initially switch relay pin OFF. 
    GPIO.output(Heater_Relay3, GPIO.LOW) # Initially switch relay pin OFF. 


def relay_switcher():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(RelayIn1, GPIO.OUT)
    GPIO.setup(RelayIn2, GPIO.OUT)
    GPIO.setup(pin1, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.output(RelayIn1, GPIO.LOW) # Initially switch relay pin OFF. 
    GPIO.output(RelayIn2, GPIO.LOW) # Initially switch relay pin OFF. 

    switch1 = GPIO.input(pin1)
    switch2 = GPIO.input(pin2)
    print("Input: switch1: ", switch1)
    print("Input: switch2: ", switch2)    
    if switch1 == 1:
        print(GPIO.HIGH, switch1)
        GPIO.output(RelayIn1, GPIO.HIGH)
        time.sleep(7.5)
        GPIO.output(RelayIn1, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()
    elif switch2 == 1:
        print(GPIO.HIGH, switch1)
        GPIO.output(RelayIn2, GPIO.HIGH)
        time.sleep(7.5)
        GPIO.output(RelayIn2, GPIO.LOW)
        time.sleep(1)
        GPIO.cleanup()    
    else:
        print("Inside else: ",GPIO.LOW, switch1)
        GPIO.output(RelayIn1, GPIO.LOW)
        GPIO.output(RelayIn2, GPIO.LOW)
        GPIO.cleanup()
        print("else")
    print("outside else")
    

def water_pump():
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
    GPIO.setup(Motor_Relay2,GPIO.OUT) # water Pump
    GPIO.setup(Switch2,GPIO.OUT)
    GPIO.output(Motor_Relay2, GPIO.LOW) # Initially switch relay pin OFF. 
    switch1 = GPIO.input(Switch2)
    print("Input: ", switch1)
    if switch1 == 1:
        print(GPIO.HIGH, switch1)
        GPIO.output(Motor_Relay2, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(Motor_Relay2, GPIO.LOW)
    else:
        print(GPIO.LOW, switch1)
        GPIO.output(Motor_Relay2, GPIO.LOW)
        time.sleep(2)

def distance_calc():
    GPIO.setmode(GPIO.BCM)              # GPIO Numbering
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
        print("StartTime:", StartTime)
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        print("StopTime", StopTime)
    
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    if distance >= 7:
        run(GPIO_ECHO)
    elif distance <= 3:
        stop(GPIO_ECHO)
    return distance


def run(GPIO_ECHO):
    # Run Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    #GPIO.output(Motor1E,GPIO.HIGH)
    sleep(0.1)
    print("Running: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)
    

def stop(GPIO_ECHO):
    # Stop Motor
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    #GPIO.output(Motor1E,GPIO.LOW)
    sleep(0.1)
    print("Stationary: GPIO_ECHO: ", GPIO_ECHO)
    #sleep(1)


def destroy():
    GPIO.cleanup()


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


def start_heater():
    GPIO.output(Heater_Relay3, GPIO.HIGH)


def halt_heater():
    GPIO.output(Heater_Relay3, GPIO.LOW)
    GPIO.cleanup()


def main():
    try:
        setup()
        while True:
            relay_switcher()
            water_pump()
            dist = distance_calc()
            print ("Measured Distance = %.1f cm" % dist)
            serialNum = sensor_temp()
            celsius = read_temp(serialNum)[0]
            farenheit = read_temp(serialNum)[1]
            if read_temp(serialNum) != None:
                print("Current temperature : %0.3f C" % celsius) # Display temp in C
                print("Current temperature : %0.3f F" % farenheit) # Display temp in F
            if celsius >= 50.0:
                halt_heater()
            elif celsius < 50.0:
                start_heater()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by User")
        destroy()
        kill_temp()
    except IndexError:
        kill_temp()
    except FileNotFoundError:
        print("Check Temp Sensor Pin 4")


if __name__ == '__main__':     # Program start from here
    main()
















