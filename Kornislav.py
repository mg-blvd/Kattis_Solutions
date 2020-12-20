nums = input().split()
for i in range(4):
    nums[i] = int(nums[i])

nums.sort()

print(nums[0] * nums[2])
