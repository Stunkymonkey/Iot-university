c1 = -8.78469475556
c2 = 1.61139411
c3 = 2.33854883889
c4 = -0.14611605
c5 = -0.012308094
c6 = -0.0164248277778
c7 = 0.002211732
c8 = 0.00072546
c9 = -0.000003582


def calculate(temperature, humidity):
    HI = c1 + (c2 * temperature) + (c3 * humidity) + (c4 * temperature * humidity) + \
        (c5 * temperature * temperature) + (c6 * humidity * humidity) + \
        (c7 * temperature * temperature * humidity) + (c8 * temperature * humidity * humidity) + \
        (c9 * temperature * temperature * humidity * humidity)
    return HI
