def check_first(num):
    if num[1] + num[2] == num[0]:
        print(f"{num[0]}={num[1]}+{num[2]}")
    elif num[1] * num[2] == num[0]:
        print(f"{num[0]}={num[1]}*{num[2]}")
    elif num[1] - num[2] == num[0]:
        print(f"{num[0]}={num[1]}-{num[2]}")
    elif num[1] / num[2] == num[0]:
        print(f"{num[0]}={num[1]}/{num[2]}")
    else:
        return False
    return True

def check_second(num):
    if num[0] + num[1] == num[2]:
        print(f"{num[0]}+{num[1]}={num[2]}")
    elif num[0] * num[1] == num[2]:
        print(f"{num[0]}*{num[1]}={num[2]}")
    elif num[0] - num[1] == num[2]:
        print(f"{num[0]}-{num[1]}={num[2]}")
    else:
        print(f"{num[0]}/{num[1]}={num[2]}")

nums = input().split()
for i in range(3):
    nums[i] = int(nums[i])

done = check_first(nums)
if not done:
    check_second(nums)
