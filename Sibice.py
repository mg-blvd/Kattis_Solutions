import sys
from math import sqrt
vals = input().split()
amount = int(vals[0])
max_length = sqrt(int(vals[1]) ** 2 + int(vals[2]) ** 2)

for i in range(amount):
    length = int(input())
    if length <= max_length:
        print('DA')
    else:
        print('NE')
