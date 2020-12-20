import sys
amount = int(input())
total = 0

for i in range(amount):
    new_num = input()
    power = int(new_num[-1])
    num = int(new_num[:-1])
    total += num ** power
print(total)
