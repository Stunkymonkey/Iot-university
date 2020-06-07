#!/usr/bin/env python3
import Adafruit_DHT
import time
import paho.mqtt.client as mqtt

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

client = mqtt.Client()
#client.on_connect = on_connect
#client.on_message = on_message

client.connect("boethin.uberspace.de", 46980, 60)
client.loop_start()

while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        client.publish("iot/temperature", temperature)
        client.publish("iot/humidity", humidity)
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);