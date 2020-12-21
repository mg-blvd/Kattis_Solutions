#work in progress
def positive_integers(num):
    sum = 0
    for i in range(num):
        sum += i + 1
    print(sum, end=' ')

def odd_integers(num):
    sum = 0
    on_num = 1
    for i in range(num):
        sum += on_num
        on_num += 2
    print(sum, end=' ')

def even_integers(num):
    sum = 0
    on_num = 2
    for i in range(num):
        sum += on_num
        on_num += 2
    print(sum)

sets = int(input())

for i in range(sets):
    new_num = input().split()
    print(new_num[0], end=' ')
    positive_integers(int(new_num[1]))
    odd_integers(int(new_num[1]))
    even_integers(int(new_num[1]))
