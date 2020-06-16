personCount = [0,0]
def getCount(index):
    return personCount[index]

def setCount(index, val):
    personCount[index] = val

states = {}
def getStates():
    return states
def setStates(key, value):
    states.update({key : value})
