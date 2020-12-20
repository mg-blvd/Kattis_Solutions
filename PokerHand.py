cards = input().split()
vals = [[], []]

for card in cards:
    if card[0] in vals[0]:
        our_index = vals[0].index(card[0])
        vals[1][our_index] += 1
    else:
        vals[0].append(card[0])
        vals[1].append(1)

print(max(vals[1]))
