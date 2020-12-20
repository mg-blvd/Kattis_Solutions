totalTests = int(input())

for i in range(totalTests):
    holder, numDays = input().split()
    numDays = int(numDays)
    total = numDays

    for i in range(1, numDays + 1):
        numDays += i

    print(holder, numDays)
