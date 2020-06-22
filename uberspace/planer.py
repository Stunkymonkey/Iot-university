#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import subprocess

import database
import export
import heat_index
import parser
import mqtt_publish

person_counter_0 = "iot/sensors/section0/counter"
person_counter_1 = "iot/sensors/section1/counter"
person_counter_2 = "iot/sensors/section2/counter"


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT-Server")
    client.subscribe("iot/sensors/#")


def save_states(topic, payload):
    if topic == "iot/sensors/section0/button/in":
        if payload == "1":
            database.increment("sensor", person_counter_0)
    elif topic == "iot/sensors/section0/button/out":
        if payload == "1":
            database.decrement("sensor", person_counter_0)
    elif topic == "iot/sensors/section1/button/in":
        if payload == "1":
            database.increment("sensor", person_counter_1)
    elif topic == "iot/sensors/section1/button/out":
        if payload == "1":
            database.decrement("sensor", person_counter_1)
    elif topic == "iot/sensors/section2/button/in":
        if payload == "1":
            database.increment("sensor", person_counter_2)
    elif topic == "iot/sensors/section2/button/out":
        if payload == "1":
            database.decrement("sensor", person_counter_2)
    else:
        database.upsert("sensor", topic, payload)


def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    # print(topic, payload)

    # save new states
    save_states(topic, payload)

    # get all values from database
    temperature = database.get("sensor", "iot/sensors/section0/temperature")
    humidity = database.get("sensor", "iot/sensors/section0/humidity")
    HI = heat_index.calculate(temperature, humidity)
    pers_s1 = database.get("sensor", person_counter_1)
    pers_s2 = database.get("sensor", person_counter_2)
    shelf_s1 = database.get("sensor", "iot/sensors/section1/shelf")
    shelf_s2 = database.get("sensor", "iot/sensors/section2/shelf")

    # save all value to file
    export.to_problem_file(HI, pers_s1, pers_s2, shelf_s1, shelf_s2)

    # run ff
    plan = subprocess.run(["./ff", "-o", "domain_supermarket.pddl", "-f",
                           "problem_supermarket_generated.pddl"], stdout=subprocess.PIPE).stdout.decode('utf-8')

    # parse resulting file
    new_states = parser.get_states(plan)
    print(new_states)

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