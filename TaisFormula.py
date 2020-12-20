from Stack import Stack

def compute_current_area(first_data, second_data):
    first_data = list(map(float, first_data))
    second_data = list(map(float, second_data))
    return ((first_data[1] + second_data[1]) / 2) * (first_data[0] - second_data[0])

def compute_total(sets, info_stack):
    total = 0
    for i in range(sets - 1):
        first = info_stack.get_top()
        second = info_stack.get_second()
        total += compute_current_area(first, second)
        info_stack.pop()
    return total / 1000


sets = int(input())
data = Stack()
for i in range(sets):
    data.push(input().split())

print(compute_total(sets, data))
