def get_ave(i, player_dice):
    placeholder = 0
    for y in range(player_dice[2 * i], player_dice[2 * i + 1] + 1):
        placeholder += y
    return (placeholder / (player_dice[2 * i + 1] - player_dice[2 * i] + 1))

gunnar_dice = list(map(int, input().split()))
emma_dice = list(map(int, input().split()))
gunnar_total = 0
emma_total = 0
for i in range(2):
    gunnar_total += get_ave(i, gunnar_dice)
    emma_total += get_ave(i, emma_dice)

if gunnar_total > emma_total:
    print("Gunnar")
elif emma_total > gunnar_total:
    print("Emma")
else:
    print("Tie")
