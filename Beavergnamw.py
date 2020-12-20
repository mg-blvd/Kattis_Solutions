import math

diameter, targetVolume = input().split()

while(diameter != '0'):
    diameter = int(diameter)
    targetVolume = int(targetVolume)
    radius = diameter / 2.0
    origVolume = (radius ** 2) * math.pi * diameter

    newVolume = origVolume - targetVolume

    newVolume /= math.pi
    newVolume /= 2
    newVolume = newVolume ** (1. / 3.)
    print(newVolume * 2)
    diameter, targetVolume = input().split()
