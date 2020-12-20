#Code still in progress

sets = int(input())

total = 0
for i in range(sets):
    info = list(map(int, input().split()))
    total += info[1] / (info[0] * 60)

print(total / sets)
