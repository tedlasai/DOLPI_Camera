#!/usr/bin/python
import RPi.GPIO as GPIO
from Adafruit_MCP4725 import MCP4725 #controls MCP4725 DAC
from time import sleep



dac = MCP4725(0x60)
# DAC output connected to frontLCD
dac.set_voltage(0)

for volt in range(0,4095,300): #Iterate through possible VCPA voltage values
    dac.set_voltage(volt)
    print ("Volt = ", volt)
    sleep(3)
    
dac.set_voltage(0) #Turn LCP off
