def find_smallest(mini, maxi, total):
    for i in range(mini, maxi + 1):
        sum = 0
        new_num = str(i)
        for digit in new_num:
            sum += int(digit)
        if sum == total:
            print(i)
            break

def find_biggest(mini, maxi, total):
    for i in range(maxi, mini - 1, -1):
        sum = 0
        new_num = str(i)
        for digit in new_num:
            sum += int(digit)
        if sum == total:
            print(i)
            break

nums = []
for i in range(3):
    nums.append(int(input()))

find_smallest(nums[0], nums[1], nums[2])
find_biggest(nums[0], nums[1], nums[2])
