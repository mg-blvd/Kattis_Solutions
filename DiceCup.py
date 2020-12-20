import sys
d1, d2 = input().split()
d1 = int(d1)
d2 = int(d2)

possibilities = []
odds = []
for i in range(1, d1 + 1):
    for j in range(1, d2 + 1):
        cur_num = i + j
        if cur_num in possibilities:
            ind = possibilities.index(cur_num)
            odds[ind] += 1
        else:
            possibilities.append(cur_num)
            odds.append(1)

highest_prob = max(odds)
for i in range(len(possibilities)):
    if odds[i] == highest_prob:
        print(possibilities[i])
