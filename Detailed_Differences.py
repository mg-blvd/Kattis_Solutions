import sys

iterations = int(input())

for i in range(iterations):
    line1, line2 = input(), input()
    similarities = ''
    for i in range(len(line1)):
        if line1[i] == line2[i]:
            similarities += '.'
        else:
            similarities += '*'
    print(line1 + '\n' + line2 + '\n' + similarities)
