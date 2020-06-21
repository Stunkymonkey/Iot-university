import paho.mqtt.client as mqtt
import states

def on_connect(client, userdata, flags, rc):
  print('client connected')
  client.subscribe("iot/#")

def on_message(client, userdata, msg):
  states.setStates(msg.topic, msg.payload.decode())
  print(states.getStates())
      

client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)

client.on_connect = on_connect
client.on_message = on_message 

client.loop_forever()