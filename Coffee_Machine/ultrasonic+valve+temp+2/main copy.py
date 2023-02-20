import RPi.GPIO as GPIO
from time import sleep
import time
import ultrasonic
import potable_h2o_heater
import milk_pump
import valve
# importing the threading module
import threading


def destroy():
    GPIO.cleanup()


def main(
    Relay1_Ln1, 
    Relay2_Ln2, 
    pin1, 
    pin2, 
    Motor_Relay2, 
    Switch2, 
    Motor1A, 
    Motor1B, 
    GPIO_TRIGGER, 
    GPIO_ECHO, 
    Relay3_Heater):
    try:
        while True:
            valve.relay_switcher(Relay1_Ln1, Relay2_Ln2, pin1, pin2)
            milk_pump.pump(Motor_Relay2, Switch2)
            dist = ultrasonic(Motor1A, Motor1B, GPIO_TRIGGER, GPIO_ECHO)
            print("Measured Distance = %.1f cm" % dist)
            serialNum = potable_h2o_heater.sensor_temp()
            celsius = potable_h2o_heater.read_temp(serialNum)[0]
            farenheit = potable_h2o_heater.read_temp(serialNum)[1]
            if potable_h2o_heater.read_temp(serialNum) != None:
                print("Current temperature : %0.3f C" % celsius) # Display temp in C
                print("Current temperature : %0.3f F" % farenheit) # Display temp in F
            if celsius >= 50.0:
                potable_h2o_heater.halt_heater(Relay3_Heater)
            elif celsius < 50.0:
                potable_h2o_heater.start_heater(Relay3_Heater)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopped by User")
        destroy()
        potable_h2o_heater.kill_temp()
    except IndexError:
        print("Index Error: Temperature Value has gone out of index. Check Temp Pin 4")
        potable_h2o_heater.kill_temp()
    except FileNotFoundError:
        print("Check Temp Sensor Pin 4")
