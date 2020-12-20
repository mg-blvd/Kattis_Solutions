import sys
lines, chars = input().split()
lines = int(lines)
chars = int(chars)

move_lines = []
moves = 1


for i in range(lines):
    move_lines.append(input())

for i in range(chars):
    equal = True
    for j in range(13):
        if move_lines[j][i] != '_':
            equal = False
            break
    if not equal:
        continue
    moves += 1
print(moves)
