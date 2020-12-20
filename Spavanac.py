import sys

hour, min = input().split()
hour = int(hour)
min = int(min)

if min < 45:
    min += 60
    hour -= 1

min -= 45

if hour == -1:
    hour = 23

print(f'{hour} {min}')
