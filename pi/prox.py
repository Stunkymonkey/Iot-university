#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

import paho.mqtt.client as mqtt

GPIO.setmode(GPIO.BOARD)

TRIG_PIN = 8
ECHO_PIN = 12

#TRIG_PIN = 16
#ECHO_PIN = 18

GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.output(TRIG_PIN, False)

GPIO.setup(ECHO_PIN, GPIO.IN)

client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_start()

while True:
    # waiting to settle sensor
    time.sleep(.1)
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = (pulse_duration * 34300) / 2
    distance = round(distance, 2)
    print ("Distance:", distance, "cm")

    client.publish("iot/sensors/section2/shelf", distance)

    time.sleep(1)

GPIO.cleanup()
