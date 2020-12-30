# in progress

space_size = 60 / 28

def getLetterValue(letter):
    if letter == ' ':
        return 27
    if letter == "'":
        return 28
    return ord(letter) - ord('A') + 1

def getSpacesAway(firstLetter, secondLetter):
    letter1 = getLetterValue(firstLetter)
    letter2 = getLetterValue(secondLetter)
    bigger = 0
    smaller = 0

    if letter2 > letter1:
        bigger = letter2
        smaller = letter1
    else:
        bigger = letter1
        smaller = letter2

    route1 = bigger - smaller
    route2 = smaller + 28 - bigger

    if route1 < route2:
        return route1
    return route2

sentence = input()
time = 0
for index in range(1, len(sentence)):
    distance = getSpacesAway(sentence[index], sentence[index - 1])
    time += (distance * space_size) / 15
    time += 1
print(time)
