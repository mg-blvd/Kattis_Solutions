steps = int(input())

for i in range(steps):
    directions = input()
    if len(directions) > 10:
        if directions[:10] == "Simon says":
            print(directions[11:])
