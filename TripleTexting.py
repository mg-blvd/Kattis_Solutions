tripleWord = input()

messageLen = len(tripleWord)
singLen = messageLen // 3

singleWords = [tripleWord[0:singLen], tripleWord[singLen:singLen * 2],
               tripleWord[singLen * 2:singLen * 3]]

if singleWords[0] == singleWords[1] or singleWords[0] == singleWords[2]:
    print(singleWords[0])
else:
    print(singleWords[1])
