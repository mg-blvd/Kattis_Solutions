colors_amount = int(input())
pink_count = 0

for iteration in range(colors_amount):
    cur_color = input()
    cur_color = cur_color.lower()

    if 'pink' in cur_color or 'rose' in cur_color:
        pink_count += 1

if pink_count == 0:
    print('I must watch Star Wars with my daughter')
else:
    print(pink_count)
