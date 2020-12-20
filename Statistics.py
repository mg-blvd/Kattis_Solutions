cases = []

while True:
    try:
        cases.append(input().split())
    except:
        break
        


for i in range(len(cases)):
    mini = int(cases[i][1])
    maxi = int(cases[i][1])
    for y in range(1, len(cases[i])):
        if mini > int(cases[i][y]):
            mini = int(cases[i][y])
        if maxi < int(cases[i][y]):
            maxi = int(cases[i][y])
    numRange = maxi - mini

    print(f"Case {i + 1}: {mini} {maxi} {numRange}")
