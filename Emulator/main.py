from tkinter import *
import mqtt 

master = Tk()
default_temp = DoubleVar()
default_temp.set(20)

default_humid = DoubleVar()
default_humid.set(40)
def getTemperature(val):
    mqtt.sendValue(val, "temperature")
def getHumidity(val):
    mqtt.sendValue(val, "humidity")
t = Scale(master, from_=0, to=40, orient=HORIZONTAL, label='temp', command=getTemperature, variable=default_temp)
t.pack()
h = Scale(master, from_=0, to=100, orient=HORIZONTAL, label='humid', command=getHumidity, variable=default_humid)
h.pack()

mainloop()
