import sys
nums = input().split()
articles = int(nums[0])
impact = int(nums[1])

if articles == 1:
    print(impact)
else:
    print(articles * (impact - 1) + 1)
