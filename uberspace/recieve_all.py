#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import states
import mqttPublish
def on_connect(client, userdata, flags, rc):
  print('client connected')
  client.subscribe("iot/#")
def publishLED():
  mqttPublish.sendValue(states.getCount(0), 'actuators/section1/led')
  mqttPublish.sendValue(states.getCount(1), 'actuators/section2/led')
  print('publishLED')
def on_message(client, userdata, msg):
  print(msg.topic + ' '  +msg.payload.decode())
  states.setStates(msg.topic, msg.payload.decode())
  if (msg.topic == 'iot/sensors/section1/button/in') and (msg.payload.decode() =='1'):
    states.setCount(0, states.getCount(0) + 1)
    publishLED()
  if (msg.topic == 'iot/sensors/section2/button/in') and (msg.payload.decode() == '1'):
    states.setCount(1, states.getCount(1) + 1)
    publishLED()
  if (msg.topic == 'iot/sensors/section1/button/out') and (msg.payload.decode() == '1'):
    states.setCount(0, states.getCount(0) - 1 )
    publishLED()
  if (msg.topic == 'iot/sensors/section2/button/out') and (msg.payload.decode() == '1'):
    states.setCount(1, states.getCount(1) - 1)
    publishLED()  
  print(states.getStates())
#client.disconnect()
    
client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
