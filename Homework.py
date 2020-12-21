prob_ranges = input().split(';')
prob_count = 0

for problems in prob_ranges:
    line_idx = problems.find('-')
    if line_idx == -1:
        prob_count += 1
        continue
    first_num = int(problems[:line_idx])
    last_num = int(problems[line_idx + 1:])
    prob_count += last_num - first_num + 1


print(prob_count)
