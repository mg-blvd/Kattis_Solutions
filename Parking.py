sets = int(input())

for i in range(sets):
    stores_num = int(input())
    spots = input().split()
    for y in range(stores_num):
        spots[y] = int(spots[y])
    print((max(spots) - min(spots)) * 2)
