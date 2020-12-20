import sys
from math import factorial
repeats = int(input())
for i in range(repeats):
    number = int(input())
    if(number < 5):
        new_num = str(factorial(number))
        print(new_num[-1])
    else:
        print(0)
