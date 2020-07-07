import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT-Server")
    client.subscribe("iot/sensors/#")
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(topic, payload)
client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()
