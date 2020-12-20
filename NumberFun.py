sets = int(input())

for y in range(sets):
    nums = input().split()
    for i in range(3):
        nums[i] = int(nums[i])
    if nums[2] >= nums[1] and nums[2] >= nums[0]:
        if nums[0] + nums[1] == nums[2] or nums[1] * nums[0] == nums[2]:
            print("Possible")
        else:
            print("Impossible")
    else:
        if nums[0] - nums[1] == nums[2] or nums[1] - nums[0] == nums[2] or nums[0] / nums[1] == nums[2] or nums[1] / nums[0] == nums[2]:
            print("Possible")
        else:
            print("Impossible")
