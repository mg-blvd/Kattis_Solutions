import sys
from statistics import mode

x = []
y = []
for i in range(3):
    nums = input().split()
    x.append(int(nums[0]))
    y.append(int(nums[1]))

most_x = mode(x)
most_y = mode(y)

for i in range(3):
    if x[i] != most_x:
        new_x = x[i]
    if y[i] != most_y:
        new_y = y[i]
print(f"{new_x} {new_y}")
