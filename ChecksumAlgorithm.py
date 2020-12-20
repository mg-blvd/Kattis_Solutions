def checksum(number):
    total = 0
    for i in range(len(number)):
        if i % 2 == 0:
            total += int(number[len(number) - i - 1])
        else:
            cur_num = int(number[len(number) - i - 1]) * 2
            if cur_num > 9:
                cur_num = (cur_num // 10) + (cur_num % 10)
            total += cur_num
    if total % 10 == 0:
        print('PASS')
    else:
        print('FAIL')

sets = int(input())

for i in range(sets):
    checksum(input())
