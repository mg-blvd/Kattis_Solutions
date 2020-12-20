num_cups = int(input())
vals_and_colors = [[], []]

for i in range(num_cups):
    new_cup = input().split()
    if new_cup[0].isnumeric():
        vals_and_colors[0].append(int(new_cup[0]) / 2)
        vals_and_colors[1].append(new_cup[1])
    else:
        vals_and_colors[0].append(int(new_cup[1]))
        vals_and_colors[1].append(new_cup[0])

for i in range(num_cups):
    smallest_cup_size = min(vals_and_colors[0])
    smallest_cup = vals_and_colors[0].index(smallest_cup_size)
    print(vals_and_colors[1][smallest_cup])
    vals_and_colors[0].pop(smallest_cup)
    vals_and_colors[1].pop(smallest_cup)
