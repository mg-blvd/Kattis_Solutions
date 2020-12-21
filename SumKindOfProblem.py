#work in progress
sets = int(input())

for i in range(sets):
    new_num = input().split()
    amount_needed = int(new_num[1])
    positive_count = 0
    odd_count = 0
    even_count = 0
    for cur_num in range(1, amount_needed * 2 + 1):
        if cur_num <= amount_needed:
            positive_count += cur_num
        if cur_num % 2 == 1:
            odd_count += cur_num
        else:
            even_count += cur_num
    print(new_num[0], positive_count, odd_count, even_count)
