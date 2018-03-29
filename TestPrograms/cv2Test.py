#!/usr/bin/python

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from time import sleep
import cv2
from Adafruit_MCP4725 import MCP4725 #controls MCP4725 DAC
import RPi.GPIO as GPIO

#MCP4725 D/A DEFINITIONS #-----------------------
# Initialize the DAC using the default address
dac = MCP4725(0x60)
# DAC output connected to frontLCD
dac.set_voltage(0)

#Raspberry Pi Camera Initialization
#----------------------------------
#Initialize the camera and grab a reference to the raw camera capture camera = PiCamera()
camera = PiCamera()
camera.resolution = (640,480)
rawCapture = PiRGBArray(camera, size=(640,480))
sleep(1)

while True:
    dac.set_voltage(0)
    sleep(0.05)
    rawCapture.truncate(0)
    camera.capture(rawCapture, format="bgr")
    image0V = rawCapture.array
    cv2.imshow("Frame0V", image0V)    
    # True grayscale conversion gives better gray balance for non-polarized light
    image0Vg=image0V[:, :, 1] #Use blue channel
    
    dac.set_voltage(3000)
    sleep(0.05)
    rawCapture.truncate(0)
    camera.capture(rawCapture, format="bgr")
    image5V = rawCapture.array
    key = cv2.waitKey(1) & 0xFF
    image5Vg=image5V[:, :, 1] #Use blue channel
    if(key == ord("q")):
        break

RGBpolV = cv2.merge([image0Vg, image0Vg, image5Vg])
cv2.imwrite("RGBpolV.jpg", RGBpolV)
cv2.imwrite("image0V.jpg", image0V)    
cv2.imwrite("image5V.jpg", image5V)
cv2.imwrite("image0Vg.jpg", image0Vg)    
cv2.imwrite("image5Vg.jpg", image5Vg)
cv2.destroyAllWindows()
quit

