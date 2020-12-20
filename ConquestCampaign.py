#WOrk in Prgress
#Try OOP

def fill_map(rows, colums, grid, counter, total):
    for x in range(rows):
        if total == counter:
            break
        for y in range(colums):
            if total == counter:
                break
            if grid[x][y]:
                if x > 0:
                    if not grid[x-1][y]:
                        grid[x-1][y] = True
                        counter += 1
                if x < rows - 1:
                    if not grid[x + 1][y]:
                        grid[x + 1][y] = True
                        counter += 1
                if y > 0:
                    if not grid[x][y - 1]:
                        grid[x][y - 1] = True
                        counter += 1
                if y < colums - 1:
                    if not grid[x][y + 1]:
                        grid[x][y + 1] = True
                        counter += 1
    return grid, counter

day = 1
counter = 0
info = list(map(int, input().split()))
total = info[0] * info[1]
grid = []
for i in range(info[0]):
    grid.append([])
    for y in range(info[1]):
        grid[i].append(False)

for i in range(info[2]):
    x, y = input().split()
    if not grid[int(x) - 1][int(y) - 1]:
        grid[int(x) - 1][int(y) - 1] = True
        counter += 1

while total != counter:
    day += 1
    grid, counter = fill_map(info[0], info[1], grid, counter, total)

print(day)
