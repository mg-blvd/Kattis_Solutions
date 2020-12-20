sets = int(input())
total = 0

for i in range(sets):
    moves = input()
    if "CD" not in moves:
        total += 1

print(total)
