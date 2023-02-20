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
import RPi.GPIO as GPIO
from time import sleep
import main

Motor1A = 2 # Pin1 for Motor Driver Inputs 
Motor1B = 3 # Pin2 for Motor Driver Inputs 
Motor_Relay2 = 8 # Relay for water Pump
Switch2 = 14
GPIO_TRIGGER = 18
GPIO_ECHO = 24
Relay1_Ln1 = 11
Relay2_Ln2 = 12
Button1 = 5
Button2 = 7
Relay3_Heater = 9 # Relay for potable water heater


if __name__ == '__main__':     # Program start from here
    main.main(
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
        Relay3_Heater)
