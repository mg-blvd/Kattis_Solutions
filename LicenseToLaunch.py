sets = int(input())
debris_nums = input().split()
for i in range(sets):
    debris_nums[i] = int(debris_nums[i])

lowest_debris = min(debris_nums)
print(debris_nums.index(lowest_debris))
