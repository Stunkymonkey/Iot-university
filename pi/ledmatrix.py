#!/usr/bin/env python3
import time

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from PIL import ImageFont
from luma.core.legacy.font import proportional, LCD_FONT
from luma.core.legacy import text
import paho.mqtt.client as mqtt
import states

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=16, height=8)

#with canvas(device) as draw:
   # draw.rectangle(device.bounding_box, outline="white", fill="black")
#    text(draw, (2,1), "0", fill="white", font=proportional(LCD_FONT))
#    text(draw, (10,1), "0", fill="white", font=proportional(LCD_FONT))

topic1 = "iot/section1/led"
topic2 = "iot/section2/led"

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe([(topic1,0), (topic2,0)])  # Subscribe to the topic “digitest/test1”, receive any messages published on it

def on_message(client, userdata, msg):
    isSet = True
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg

def on_message_n1(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    tmp = msg.payload
    print(type(tmp))
    tmp = int(tmp)
    print(type(tmp))
    states.setCount(0, tmp)    
    with canvas(device) as draw:
        text(draw, (2,1), str(states.getCount(0)), fill="white", font=proportional(LCD_FONT))
        text(draw, (10,1), str(states.getCount(1)), fill="white", font=proportional(LCD_FONT))
def on_message_n2(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    msg.payload = msg.payload.decode("utf-8")
    tmp = msg.payload
    print(type(tmp))
    tmp = int(tmp)
    print(type(tmp))
    states.setCount(1, tmp)
    with canvas(device) as draw:
        text(draw, (2,1), str(states.getCount(0)), fill="white", font=proportional(LCD_FONT))
        text(draw, (10,1), str(states.getCount(1)), fill="white", font=proportional(LCD_FONT))




client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add(topic1, on_message_n1)
client.message_callback_add(topic2, on_message_n2)

client.on_message = on_message
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_forever()

# virtual = viewport(device, width=200, height=100)


