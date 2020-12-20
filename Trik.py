positions = [1, 0, 0]
moves = input()

def switch_places(char):
    if char == "A":
        positions[0], positions[1] = positions[1], positions[0]
    elif char == "B":
        positions[1], positions[2] = positions[2], positions[1]
    elif char == 'C':
        positions[0], positions[2] = positions[2], positions[0]

for i in moves:
    switch_places(i)

place = positions.index(1)
print(place + 1)
