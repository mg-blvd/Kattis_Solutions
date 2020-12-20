found = False

for i in range(5):
    newName = input()
    if "FBI" in newName:
        print(i + 1, end=" ")
        found = True

if not found:
    print("HE GOT AWAY!")
