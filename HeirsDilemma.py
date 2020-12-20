counter = 0
nums = list(map(int, input().split()))

for i in range(nums[0], nums[1] + 1):
    str_num = str(i)
    if '0' not in str_num:
        for index in range(5):
            if str_num[index] not in str_num[index + 1:]:
                if index == 4:
                    if i % int(str_num[index]) == 0 and i % int(str_num[index + 1]) == 0:
                        counter += 1
                elif i % int(str_num[index]) != 0:
                    break
            else:
                break
print(counter)
