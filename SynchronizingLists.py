amountOfPairs = int(input())

while amountOfPairs != 0:
    firstList = []
    secondList = []
    keyValues = {}

    for i in range(amountOfPairs):
        newNum = int(input())
        firstList.append(newNum)

    firstHolder = firstList.copy()

    for i in range(amountOfPairs):
        newNum = int(input())
        secondList.append(newNum)

    firstHolder.sort()
    secondList.sort()

    for i in range(len(firstHolder)):
        keyValues[firstHolder[i]] = secondList[i]

    for i in range(len(firstList)):
        print(keyValues[firstList[i]])
    print("")

    amountOfPairs = int(input())
