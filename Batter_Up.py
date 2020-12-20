import sys

at_bats = int(input())
vals = input().split()
total = 0

for i in vals:
    number = int(i)
    if number == -1:
        at_bats -= 1
    else:
        total += number

print(total / at_bats)
