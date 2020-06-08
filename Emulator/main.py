from tkinter import *
import mqtt 

master = Tk()
default_temp = DoubleVar()
default_temp.set(20)

default_humid = DoubleVar()
default_humid.set(40)
def getValue(val):
    print(val)
    mqtt.sendValue()
w = Scale(master, from_=15, to=30, orient=HORIZONTAL, label='temp', command=getValue, variable=default_temp)
w.pack()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL, label='humid', command=getValue, variable=default_humid)
w.pack()

mainloop()
