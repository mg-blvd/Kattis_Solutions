#work in progress
def add_digits(number):
    curr_total = 0
    for i in str(number):
        curr_total += int(i)
    return curr_total


iterations = int(input())

for i in range(iterations):
    total = 0
    nums = input().split()
    for i in range(int(nums[0]), int(nums[1]) + 1):
        total += add_digits(i)
    print(total)
