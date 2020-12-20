def shiftCharVal(shiftChar, curChar):
    shiftVal = ord(shiftChar) - 65
    newLetterVal = ord(curChar) - shiftVal
    if newLetterVal < 65:
        difference = 65 - newLetterVal
        newLetterVal = 91 - difference

    return chr(newLetterVal)

encryptMes = input()
key = input()

actualMes = ""
curShift = ""

for i in range(len(encryptMes)):
    if i < len(key):
        curShift = key[i]
    else:
        curShift = actualMes[i - len(key)]
    actualMes += shiftCharVal(curShift, encryptMes[i])

print(actualMes)
