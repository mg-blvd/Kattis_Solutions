starter = int(input())

while(True):
    total = 0
    for i in str(starter):
        total += int(i)
    if starter % total == 0:
        print(starter)
        break
    starter += 1
