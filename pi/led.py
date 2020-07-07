#!/usr/bin/env python3
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

PIN_GREEN = 32
PIN_RED = 36

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(PIN_GREEN, GPIO.OUT)
GPIO.setup(PIN_RED, GPIO.OUT)

topic = "iot/actuators/section0/gate"

def on_connect(client, userdata, flags, rc):
    print("connected with result code {0}".format(str(rc)))
    client.subscribe([(topic, 0)])

def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    if msg.payload == "-":
        GPIO.output(PIN_GREEN, GPIO.LOW)
        GPIO.output(PIN_RED, GPIO.HIGH)
    else:
        GPIO.output(PIN_GREEN, GPIO.HIGH)
        GPIO.output(PIN_RED, GPIO.LOW)

client = mqtt.Client()
client.on_connect = on_connect

client.on_message = on_message
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_forever()
