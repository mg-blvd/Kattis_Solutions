letterCount = []
for i in range(26):
    letterCount.append(0)

inputWord = input()

for letter in inputWord:
    letterCount[ord(letter) - ord('a')] += 1

oddsCount = 0;
for num in letterCount:
    if num % 2 == 1:
        oddsCount += 1

print(oddsCount - 1)
