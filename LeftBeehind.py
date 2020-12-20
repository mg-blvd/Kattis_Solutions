nums = input().split()

while nums != ["0", "0"]:
    first = int(nums[0])
    second = int(nums[1])
    if first + second == 13:
        print('Never speak again.')
    elif first > second:
        print('To the convention.')
    elif second > first:
        print('Left beehind.')
    else:
        print('Undecided.')
    nums = input().split()
