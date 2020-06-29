#!/usr/bin/env python3
# arg1: section: 1,2
# arg2: in, out

import signal
import sys
import RPi.GPIO as GPIO
import states
import mqttPublish
import time

gpio_in_list = [38, 37, 33]
gpio_out_list = [40, 35, 31]

def getGPIO(section):
    if (property == "in"):
        return gpio_in_list[section]
    elif (property == "out"):
        return gpio_out_list[section]


if (len(sys.argv) != 3):
    BUTTON_GPIO = 16
else:
    section = int(sys.argv[1])
    property = sys.argv[2]
    BUTTON_GPIO = getGPIO(section)
name = 'section' + str(section) + '/button/' + property

def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)

def button_action(channel):
    #time.sleep(.01)
    if not GPIO.input(channel):
        mqttPublish.sendValue(1, name)
        print("Button pressed!", section, property)
    else:
        mqttPublish.sendValue(0, name)
        print("       Button released!", section, property)

if __name__ == "__main__":
    print('button started', section, property)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    try:
        state = GPIO.input(BUTTON_GPIO)
        while True:
            new_state = GPIO.input(BUTTON_GPIO)
            if state != new_state:
                if not new_state:
                    mqttPublish.sendValue(1, name)
                    print("Button pressed!", section, property)
                else:
                    mqttPublish.sendValue(0, name)
                    print("       Button released!", section, property)
                state = new_state
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Cleaning up")
        GPIO.cleanup()

    #GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_action, bouncetime=50)

    #signal.signal(signal.SIGINT, signal_handler)
    #signal.pause()
