#!/usr/bin/env python3

import paho.mqtt.client as mqtt

import database
import export
import parser
import mqtt_publish


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT-Server")
    client.subscribe("iot/sensors/#")


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(topic, payload)
    # move the following to seperate file and complete
    if (topic == "iot/section1/button/in") and (payload == "1"):
        database.increment("sensor", "iot/sensors/section1/button")
    if (topic == "iot/section2/button/in") and (payload == "1"):
        database.increment("sensor", "iot/sensors/section2/button")
    if (topic == "iot/section1/button/out") and (payload == "1"):
        database.decrement("sensor", "iot/sensors/section1/button")
    if (topic == "iot/section2/button/out") and (payload == "1"):
        database.decrement("sensor", "iot/sensors/section1/button")
    if (topic == "iot/sensors/section1/shelf"):
        database.upsert("sensor", "iot/sensors/section1/shelf", payload)
    # get all values from database
    export.to_problem_file(1, 2, 3, 4, 5)
    # todo run ff
    # parse resulting file
    # check what should get updated with database
    # send new updates like this (maybe from different file)
    topic = "iot/sensors/section1/led"
    mqtt_publish.sendValue(database.get("sensor", topic), topic)
    topic = "iot/sensors/section2/led"
    mqtt_publish.sendValue(database.get("sensor", topic), topic)


client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
# client.disconnect()
