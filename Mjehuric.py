#work in progress
def print_list(list):
    for i in range(5):
        if i == 4:
            print(list[i])
        else:
            print(list[i], end=' ')

order = list(map(int, input().split()))

while sorted(order) != order:
    for i in range(5):
        if order[i] > order[i + 1]:
            place = order[i + 1]
            order[i + 1] = order[i]
            order[i] = place
            break
    print_list(order)
