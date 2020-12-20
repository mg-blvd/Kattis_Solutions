import math
numOfStars = int(input())
maxStars = math.ceil(numOfStars)

print(str(numOfStars) + ":")

for int in range(2, maxStars):
    intsPair = int - 1
    pairTotal = intsPair + int
    totalDivides = math.floor(numOfStars / pairTotal)

    if numOfStars % (pairTotal) == 0 or \
            totalDivides * pairTotal + int == numOfStars:
        print(str(int) + "," + str(intsPair))
    if numOfStars % int == 0:
        print(str(int) + "," + str(int))
