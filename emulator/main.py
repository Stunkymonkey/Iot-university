#!/usr/bin/env python3

from tkinter import *
import mqtt_publish as mqtt
out_color = '#c62828'
in_color = '#4caf50'
nearMax = 20
nearMin = 2


class CrowsEmulator:

    def __init__(self, master):
        self.master = master
        master.title("Crows Emulator")

        self.default_temp = DoubleVar()
        self.default_temp.set(20)

        self.default_humid = DoubleVar()
        self.default_humid.set(40)

        self.default_near1 = DoubleVar()
        self.default_near1.set(5)

        self.default_near2 = DoubleVar()
        self.default_near2.set(5)

        self.led1 = StringVar()
        self.led1.set('0')

        self.one = DoubleVar()
        self.one.set(1)

        self.section0 = Label(master, text="Section 0")
        self.section0.grid(sticky=W, pady=4, padx=5)

        self.t = Scale(master, from_=0, to=40, orient=HORIZONTAL, label='temp',
                       command=self.getTemperature, variable=self.default_temp)
        self.t.grid(row=1, column=1, columnspan=2, sticky=W)
        self.h = Scale(master, from_=0, to=100, orient=HORIZONTAL, label='humid',
                       command=self.getHumidity, variable=self.default_humid)
        self.h.grid(row=1, column=3)

        self.b0_out = Button(master, text="person out s0", command=self.decreaseS1, bg=out_color)
        self.b0_out.grid(row=2, column=1)
        self.b0_in = Button(master, text="person in s0", command=self.increaseS1, bg=in_color)
        self.b0_in.grid(row=2, column=3)

        self.section1 = Label(master, text="Section 1")
        self.section1.grid(sticky=W, pady=4, padx=5, row=4)

        self.nplus = Button(master, text="+", command=self.addoneNear1)
        self.nplus.grid(row=5, column=3, sticky=W + S)

        self.nminus = Button(master, text="-", command=self.minusoneNear1)
        self.nminus.grid(row=5, column=1, sticky=E + S)

        self.n = Scale(master, from_=nearMin, to=nearMax, orient=HORIZONTAL,
                       label='Shelf section 1', command=self.getShelf1, variable=self.default_near1)
        self.n.grid(row=5, column=2)

        self.b1_out = Button(master, text="person out s1", command=self.decreaseS1, bg=out_color)
        self.b1_out.grid(row=6, column=1)
        self.b1_in = Button(master, text="person in s1", command=self.increaseS1, bg=in_color)
        self.b1_in.grid(row=6, column=3)

        self.section2 = Label(master, text="Section 2")
        self.section2.grid(sticky=W, pady=4, padx=5, row=7)

        self.n2plus = Button(master, text="+", command=self.addoneNear2)
        self.n2plus.grid(row=8, column=3, sticky=W + S)

        self.n2minus = Button(master, text="-", command=self.minusoneNear2)
        self.n2minus.grid(row=8, column=1, sticky=E + S)

        self.n2 = Scale(master, from_=nearMin, to=nearMax, orient=HORIZONTAL,
                        label='Shelf section 2', command=self.getShelf2, variable=self.default_near2)
        self.n2.grid(row=8, column=2)

        self.b2_out = Button(master, text="person out s2", command=self.decreaseS2, bg=out_color)
        self.b2_out.grid(row=9, column=1)
        self.b2_in = Button(master, text="person in s2", command=self.increaseS2, bg=in_color)
        self.b2_in.grid(row=9, column=3)

    def addoneNear1(self):
        self.default_near1.set(self.default_near1.get() + self.one.get())
        self.getShelf1(int(self.default_near1.get()))

    def addoneNear2(self):
        self.default_near2.set(self.default_near2.get() + self.one.get())
        self.getShelf2(int(self.default_near2.get()))

    def minusoneNear1(self):
        self.default_near1.set(self.default_near1.get() - self.one.get())
        self.getShelf1(int(self.default_near1.get()))

    def minusoneNear2(self):
        self.default_near2.set(self.default_near2.get() - self.one.get())
        self.getShelf2(int(self.default_near2.get()))

    def getTemperature(self, val):
        mqtt.sendValue(val, "section0/temperature")

    def getHumidity(self, val):
        mqtt.sendValue(val, "section0/humidity")

    def getShelf1(self, val):
        mqtt.sendValue(val, "section1/shelf")

    def getShelf2(self, val):
        mqtt.sendValue(val, "section2/shelf")

    def increaseS0(self):
        mqtt.sendButtons("section0/button/in")

    def decreaseS0(self):
        mqtt.sendButtons("section0/button/out")

    def increaseS1(self):
        mqtt.sendButtons("section1/button/in")

    def decreaseS1(self):
        mqtt.sendButtons("section1/button/out")

    def increaseS2(self):
        mqtt.sendButtons("section2/button/in")

    def decreaseS2(self):
        mqtt.sendButtons("section2/button/out")


root = Tk()
my_gui = CrowsEmulator(root)
root.mainloop()
