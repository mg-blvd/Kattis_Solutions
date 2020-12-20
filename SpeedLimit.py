sets = int(input())

while sets != -1:
    last_time = 0
    miles_total = 0
    for i in range(sets):
        curr_set = input().split()
        elapsed_hours = int(curr_set[1])
        miles_total += int(curr_set[0]) * (elapsed_hours - last_time)
        last_time = elapsed_hours
    print(f"{miles_total} miles")
    sets = int(input())
