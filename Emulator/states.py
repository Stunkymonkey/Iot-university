from tkinter import *
states = {}

def getState(s):
    return states[s]
def getStates():
    return states
def setStates(key, value):
    states.update({key : value})
    getLed()
    print(states)

