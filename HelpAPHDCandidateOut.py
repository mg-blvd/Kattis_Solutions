def add_nums(equation):
    divider = equation.index('+')
    print(int(equation[:divider]) + int(equation[divider + 1:]))

sets = int(input())

for i in range(sets):
    equation = input()
    if '+' in equation:
        add_nums(equation)
    else:
        print("skipped")
