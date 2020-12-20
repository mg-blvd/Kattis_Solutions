import sys

amount = int(input())

for i in range(amount):
    nums = input().split()
    no_ads = int(nums[0])
    net_ads = int(nums[1]) - int(nums[2])
    if no_ads > net_ads:
        print('do not advertise')
    elif net_ads > no_ads:
        print('advertise')
    else:
        print('does not matter')
