def find_sum_integers(number):
    sum = 0
    number = str(number)
    for digit in number:
        sum += int(digit)
    return sum

test_case = int(input())

while test_case != 0:
    target = find_sum_integers(test_case)
    done = False
    counter = 11
    while not done:
        if find_sum_integers(test_case * counter) == target:
            print(counter)
            done = True
        else:
            counter += 1
    test_case = int(input())
