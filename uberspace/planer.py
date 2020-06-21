#!/usr/bin/env python3

import paho.mqtt.client as mqtt

import database
import export
import parser
import mqtt_publish
import subprocess


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT-Server")
    client.subscribe("iot/sensors/#")


def save_states(topic, payload):
    if topic == "iot/sensors/section0/button/in":
        if payload == "1":
            database.increment("sensor", "iot/sensors/section0/counter")
    elif topic == "iot/sensors/section0/button/out":
        if payload == "1":
            database.decrement("sensor", "iot/sensors/section0/counter")
    elif topic == "iot/sensors/section1/button/in":
        if payload == "1":
            database.increment("sensor", "iot/sensors/section1/counter")
    elif topic == "iot/sensors/section1/button/out":
        if payload == "1":
            database.decrement("sensor", "iot/sensors/section1/counter")
    elif topic == "iot/sensors/section2/button/in":
        if payload == "1":
            database.increment("sensor", "iot/sensors/section2/counter")
    elif topic == "iot/sensors/section2/button/out":
        if payload == "1":
            database.decrement("sensor", "iot/sensors/section2/counter")
    else:
        database.upsert("sensor", topic, payload)


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(topic, payload)

    # save new states
    save_states(topic, payload)
    # get all values from database
    humidity = database.get("sensor", "iot/sensors/section0/humidity")
    temperature = database.get("sensor", "iot/sensors/section0/temperature")
    heat_index = humidity
    pers_s1 = database.get("sensor", "iot/sensors/section1/counter")
    pers_s2 = database.get("sensor", "iot/sensors/section2/counter")
    shelf_s1 = database.get("sensor", "iot/sensors/section1/shelf")
    shelf_s2 = database.get("sensor", "iot/sensors/section2/shelf")
    # heat_index, pers_s1, pers_s2, , 
    export.to_problem_file(heat_index, pers_s1, pers_s2, shelf_s1, shelf_s2)
    # run ff
    result = subprocess.call(["./ff", "-o", "domain_supermarket.pddl", "-f",
                              "problem_supermarket_generated.pddl"], stdout=subprocess.PIPE)
    plan = result.stdout
    print(plan)
    # parse resulting file
    # check what should get updated with database
    # send new updates like this (maybe from different file)
    topic = "iot/actuators/section1/led"
    mqtt_publish.sendValue(database.get("sensor", topic), topic)
    topic = "iot/actuators/section2/led"
    mqtt_publish.sendValue(database.get("sensor", topic), topic)


client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
# client.disconnect()
