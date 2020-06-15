from tkinter import *
import mqtt 

master = Tk()
default_temp = DoubleVar()
default_temp.set(20)

default_humid = DoubleVar()
default_humid.set(40)

default_near = DoubleVar()
default_near.set(10)

def getTemperature(val):
    mqtt.sendValue(val, "temperature")
def getHumidity(val):
    mqtt.sendValue(val, "humidity")
def getNear(val):
    mqtt.sendValue(val, "near")
t = Scale(master, from_=0, to=40, orient=HORIZONTAL, label='temp', command=getTemperature, variable=default_temp)
t.pack()
h = Scale(master, from_=0, to=100, orient=HORIZONTAL, label='humid', command=getHumidity, variable=default_humid)
h.pack()
n = Scale(master, from_=0, to=20, orient=HORIZONTAL, label='near', command=getHumidity, variable=default_humid)
n.pack()

mainloop()
