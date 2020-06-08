import paho.mqtt.client as mqtt
client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)
