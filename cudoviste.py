rows, columns = input().split()

parkingSquishes = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0
}

row1 = input()

for rowNum in range(1, int(rows)):
    row2 = input()
    for columnNum in range(int(columns) - 1):
        numOfCars = 0
        buildingInWay = False

        spacesToTake = row1[columnNum: columnNum + 2] + \
            row2[columnNum: columnNum + 2]

        for currentSpace in spacesToTake:
            if currentSpace == '#':
                buildingInWay = True
                break
            elif currentSpace == 'X':
                numOfCars += 1

        if not buildingInWay:
            parkingSquishes[numOfCars] += 1

    row1 = row2

for key in parkingSquishes:
    print(parkingSquishes[key])
