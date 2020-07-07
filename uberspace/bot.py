#!/usr/bin/env python3
# -*- coding: utf-8 -*

import requests
import json
import paho.mqtt.client as mqtt

topic1 = "iot/actuators/section1/refill_shelf"
topic2 = "iot/actuators/section2/refill_shelf"

def send_message(section):
    token = '1289247562:AAG7c3kcAHd2Q96CBLl05jaPH4JBQEGL6E0'
    sendUrl = f'https://api.telegram.org/bot{token}/sendMessage'
    chat_id = '-487882837'
    message = 'please refill shelf in section {}'
    data = {'chat_id': {chat_id}, 'text': {message.format(section)}}
    requests.post(sendUrl, data).json() 

def on_message(client, userdata, message):
    topic = message.topic
    print('topic: ' + topic)

    
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe([(topic1,0), (topic2,0)]) 
    
def on_message_s1(client, userdata, msg):
    print("s1", msg.payload.decode("utf-8"))
    if msg.payload.decode("utf-8") == "True":
        send_message("1")

def on_message_s2(client, userdata, msg):
    print("s2", msg.payload.decode("utf-8"))
    if msg.payload.decode("utf-8") == "True":
        send_message("2")
    

if __name__ == '__main__':
    mqtt_subscriber = mqtt.Client()
    mqtt_subscriber.on_message = on_message
    mqtt_subscriber.message_callback_add(topic1, on_message_s1)
    mqtt_subscriber.message_callback_add(topic2, on_message_s2)
    mqtt_subscriber.on_connect = on_connect
   
    mqtt_subscriber.connect("boethin.uberspace.de", 46980, 60)
    
    mqtt_subscriber.loop_forever()
