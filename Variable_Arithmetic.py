import sys
var_names = []
var_val = []
new_line = input()

def change_val(line):
    new_line = line.split()
    if new_line[0] in var_names:
        index = var_names.find(new_line[0])
        var_val[index] = int(new_line[1])
    else:
        var_names.append(new_line[0])
        var_val.append(int(new_line[1]))

def add_nums(arr):
    total = 0
    placeholder = []
    for i in arr:
        if i.isnumeric():
            total += int(i)
            placeholder.append(True)
        else:
            if i in var_names:
                index = var_names.find(i)
                total += var_val[index]
                placeholder.append(True)
            else:
                placeholder.append(False)
    out = str(total)
    for i in range(len(placeholder)):
        if not placeholder[i]:
            out += arr[i]
    print(out)

while new_line != '0':
    if '=' in new_line:
        change_val(new_line)
    else:
        add_nums(new_line.split())
    new_line = input()
