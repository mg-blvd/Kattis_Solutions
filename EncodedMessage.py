from math import sqrt

messagesNum = int(input())

for i in range(messagesNum):
    scrambledMessage = input()
    message = ""

    dimension = int(sqrt(len(scrambledMessage)))

    for i in range(dimension - 1, -1, -1):
        index = i
        while index < len(scrambledMessage):
            message += scrambledMessage[index]
            index += dimension

    print(message)
