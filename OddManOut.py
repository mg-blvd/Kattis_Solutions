sets = int(input())

for y in range(sets):
    invitees = int(input())
    invitees_ids = input().split()
    invitees_ids.sort()
    for i in range(0, invitees, 2):
        if i == invitees - 1 or invitees_ids[i] != invitees_ids[i + 1]:
            alone = invitees_ids[i]
            break
    print(f"Case #{y + 1}: {alone}")
