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

states = ["0", "0"]

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=16, height=8, block_orientation=-90)

with canvas(device) as draw:
    text(draw, (2,1), "0", fill="white", font=proportional(LCD_FONT))
    text(draw, (10,1), "0", fill="white", font=proportional(LCD_FONT))

topic1 = "iot/actuators/section1/gate"
topic2 = "iot/actuators/section2/gate"

def on_connect(client, userdata, flags, rc):
    print("connected with result code {0}".format(str(rc)))
    client.subscribe([(topic1,0), (topic2,0)])

def on_message(client, userdata, msg):
    isset = true
    print("message received-> " + msg.topic + " " + str(msg.payload))

def on_message_n1(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    states[0] = msg.payload
    draw()
def on_message_n2(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")
    states[1] = msg.payload
    draw()

def draw():
    with canvas(device) as draw:
        text(draw, (10,1), str(states[0]), fill="white", font=proportional(LCD_FONT))
        text(draw, (2,1), str(states[1]), fill="white", font=proportional(LCD_FONT))




client = mqtt.Client()
client.on_connect = on_connect
client.message_callback_add(topic1, on_message_n1)
client.message_callback_add(topic2, on_message_n2)

client.on_message = on_message
client.connect("boethin.uberspace.de", 46980, 60)
client.loop_forever()

# virtual = viewport(device, width=200, height=100)


