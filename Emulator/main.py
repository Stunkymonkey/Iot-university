from tkinter import *
import mqtt_publish as mqtt
master = Tk()

default_temp = DoubleVar()
default_temp.set(20)

default_humid = DoubleVar()
default_humid.set(40)

default_near1 = DoubleVar()
default_near1.set(10)

default_near2 = DoubleVar()
default_near2.set(10)

led1 = StringVar()
led1.set('0')

def getTemperature(val):
    mqtt.sendValue(val, "section0/temperature")
def getHumidity(val):
    mqtt.sendValue(val, "section0/humidity")
def getShelf1(val):
    mqtt.sendValue(val, "section1/shelf")
def getShelf2(val):
    mqtt.sendValue(val, "section2/shelf")
def increaseS0():
    mqtt.sendButtons("section0/button/in")
def decreaseS0():
    mqtt.sendButtons("section0/button/out")
def increaseS1():
    mqtt.sendButtons("section1/button/in")
def decreaseS1():
    mqtt.sendButtons("section1/button/out")
def increaseS2():
    mqtt.sendButtons("section2/button/in")
def decreaseS2():
    mqtt.sendButtons("section2/button/out")


    
section0 = Label(master, text="Section 0")
section0.grid(sticky=W, pady=4, padx=5)
t = Scale(master, from_=0, to=40, orient=HORIZONTAL, label='temp', command=getTemperature, variable=default_temp)
t.grid(row=1, column=1, columnspan=2, sticky=W)
h = Scale(master, from_=0, to=100, orient=HORIZONTAL, label='humid', command=getHumidity, variable=default_humid)
h.grid(row=1, column=3)

b0_out = Button(master, text="person out s0", command=decreaseS1)
b0_out.grid(row=2, column=1)
b0_in = Button(master, text="person in s0", command=increaseS1)
b0_in.grid(row=2, column=3)

section1 = Label(master, text="Section 1")
section1.grid(sticky=W, pady=4, padx=5, row=4)

n = Scale(master, from_=0, to=20, orient=HORIZONTAL, label='Shelf section 1', command=getShelf1, variable=default_near1)
n.grid(row=5, column=2)

b1_out = Button(master, text="person out s1", command=decreaseS1)
b1_out.grid(row=6, column=1)
b1_in = Button(master, text="person in s1", command=increaseS1)
b1_in.grid(row=6, column=3)

section2 = Label(master, text="Section 2")
section2.grid(sticky=W, pady=4, padx=5, row=7)

n = Scale(master, from_=0, to=20, orient=HORIZONTAL, label='Shelf section 2', command=getShelf2, variable=default_near2)
n.grid(row=8, column=2)

b2_out = Button(master, text="person out s2", command=decreaseS2)
b2_out.grid(row=9, column=1)
b2_in = Button(master, text="person in s2", command=increaseS2)
b2_in.grid(row=9, column=3)


mainloop()
