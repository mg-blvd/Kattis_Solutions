import math

numMessages = int(input())

for i in range(numMessages):
    inputMes = input()
    outputMes = ""
    mesLen = len(inputMes)
    targetLen = int(math.pow(math.floor(math.sqrt(mesLen)) + 1, 2))
    sqrtOfTargetLen = int(math.floor(math.sqrt(targetLen)))

    while(len(inputMes) < targetLen):
        inputMes += "*"

    for i in range(targetLen - sqrtOfTargetLen, targetLen):
        for y in range(i, -1, -sqrtOfTargetLen):
            if(inputMes[y] != '*'):
                outputMes += inputMes[y]

    print(outputMes)
