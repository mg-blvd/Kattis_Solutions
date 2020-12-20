numOfInput = int(input())
scores = []

for i in range(numOfInput):
    scores.append(int(input()))

summation = 0
originalTotal = 0

for i in range(numOfInput):
    originalTotal += scores[i] * ((4. / 5.) ** i)
    currentTotal = 0
    currentExp = 0

    for idx in range(numOfInput):
        if idx != i:
            currentTotal += scores[idx] * ((4. / 5.) ** currentExp)
            currentExp += 1

    summation += currentTotal / 5.


print(originalTotal / 5)
print(summation / numOfInput)
