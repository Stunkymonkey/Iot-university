import paho.mqtt.client as mqtt
import time
client = mqtt.Client()
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_start()

def sendValue(val, name):
    client.publish("iot/sensors/"+name, val)

def sendButtons(name):
    client.publish("iot/sensors/"+name, "1")
    time.sleep(1)
    client.publish("iot/sensors/"+name, "0")


