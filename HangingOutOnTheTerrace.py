nums = input().split()
total = 0
rejects = 0

for i in range(int(nums[1])):
    event = input().split()
    if event[0] == "enter":
        if total + int(event[1]) <= int(nums[0]):
            total += int(event[1])
        else:
            rejects += 1
    else:
        total -= int(event[1])

print(rejects)
