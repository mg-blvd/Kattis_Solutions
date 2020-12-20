def get_display_line(line, stretch):
    display_line = ""
    for i in line:
        display_line += i * stretch
    return display_line

important_nums = input().split()
for i in range(4):
    important_nums[i] = int(important_nums[i])

for i in range(important_nums[0]):
    sample_line = input()
    line_for_print = get_display_line(sample_line, important_nums[3])
    for y in range(important_nums[2]):
        print(line_for_print)
