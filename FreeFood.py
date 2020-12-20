sets = int(input())
days = []

for i in range(sets):
    dates = list(map(int, input().split()))
    for day in range(dates[0], dates[1] + 1):
        if day not in days:
            days.append(day)

print(len(days))
