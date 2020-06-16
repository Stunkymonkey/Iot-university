#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt
 
GPIO.setmode(GPIO.BCM)

TRIG1 = 14
ECHO1 = 18

GPIO.setwarnings(False)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.output(TRIG1, False)

GPIO.setup(ECHO1, GPIO.IN)

client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_start()

while True:
    # waiting to settle sensor
    time.sleep(.1)
    GPIO.output(TRIG1, True)
    time.sleep(0.00001)
    GPIO.output(TRIG1, False)

    while GPIO.input(ECHO1) == 0:
        pulse_start1 = time.time()
     
    while GPIO.input(ECHO1) == 1:
        pulse_end1 = time.time()

    pulse_duration1 = pulse_end1 - pulse_start1

    distance1 = pulse_duration1 * 17150
    distance1= round(distance1, 2)
    print ("Distance1:",distance1, "cm")

    client.publish("iot/shelf/section1", distance1)

    time.sleep(1)

GPIO.cleanup()
