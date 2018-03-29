#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

calLEDpin=23 #Calibration LED connected to pin 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(calLEDpin,GPIO.OUT)
GPIO.output(calLEDpin,True) #Turn calibration LED on
