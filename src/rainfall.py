#!/usr/bin/env python
# coding: utf-8
# info
__version__ = "0.1"
__author__  = "Akli R"
__date__    = "04/10/19"

from gpiozero import Button
import time

BUCKET_SIZE = 0.2794
rain_count = 0
rain_interval = 5

def bucket_tipped():
    global rain_count
    rain_count += 1

def reset_rainfall():
    global rain_count
    rain_count = 0

def calculate_rainfall():
    global rain_count
    rainfall = rain_count * BUCKET_SIZE
    
    return rainfall


rain_sensor = Button(6)
rain_sensor.when_pressed = bucket_tipped

while True:
    rain_count = 0
    time.sleep(rain_interval)
    print(calculate_rainfall(), "mm")