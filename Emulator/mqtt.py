import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_start()

def sendValue(val, name):
    client.publish("iot/"+name, val)

