import RPi.GPIO as GPIO
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
    Button1, 
    Button2, 
    Motor_Relay2, 
    Switch2, 
    Motor1A, 
    Motor1B, 
    GPIO_TRIGGER, 
    GPIO_ECHO, 
    Relay3_Heater):

    try:
        while True:
            # Given below are threads valv, milk, dist and heater:
            valv = threading.Thread(target=valve.relay_switcher, args=(Relay1_Ln1, Relay2_Ln2, Button1, Button2))
            milk = threading.Thread(target=milk_pump.pump, args=(Motor_Relay2, Switch2))
            dist = threading.Thread(target=ultrasonic.distance_calc, args=(Motor1A, Motor1B, GPIO_TRIGGER, GPIO_ECHO))
            heater = threading.Thread(target=potable_h2o_heater.temp_control, args=(Relay3_Heater))

            # start the threads
            valv.start()
            milk.start()
            dist.start()
            heater.start()

            # wait for the threads to finish
            valv.join()
            milk.join()
            dist.join()
            heater.join()

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
