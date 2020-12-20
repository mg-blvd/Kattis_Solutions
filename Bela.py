regular_cards = {
'A' : 11,
"K" : 4,
"Q" : 3,
"J" : 2,
"T" : 10,
"9" : 0,
"8" : 0,
"7" : 0
}

dominant_cards = {
"J" : 20,
"9" : 14
}

points = 0
hands, dominant = input().split()
hands = int(hands)

for i in range(4 * hands):
    curr_card = input()
    if curr_card[1] == dominant and (curr_card[0] == 'J' or curr_card[0] == '9'):
        points += dominant_cards[curr_card[0]]
    else:
        points += regular_cards[curr_card[0]]

print(points)
