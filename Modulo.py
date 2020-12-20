nums = []

for i in range(10):
    new_num = int(input())
    if new_num % 42 not in nums:
        nums.append(new_num % 42)

print(len(nums))
