cases = int(input())

for i in range(cases):
    total = 0
    turtles = input().split()
    for i in range(len(turtles)):
        turtles[i] = int(turtles[i])

    for i in range(len(turtles) - 1):
        if turtles[i + 1] > 2 * turtles[i]:
            total += turtles[i + 1] - (turtles[i] * 2)
    print(total)
