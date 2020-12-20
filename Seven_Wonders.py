import math
cards = input()

totals = [0, 0, 0]
total = 0

def find_val(num):
    sum = 0
    if num >= 1:
        sum = pow(num, 2)
    return sum

for letter in cards:
    if letter == 'T':
        totals[0] += 1
    elif letter == 'C':
        totals[1] += 1
    else:
        totals[2] += 1

sets = min(totals)

total += find_val(totals[0])
total += find_val(totals[1])
total += find_val(totals[2])
print(total + sets * 7)
