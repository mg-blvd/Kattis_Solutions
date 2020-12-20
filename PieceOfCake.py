cake_length, vertical_cut, horizontal_cut = input().split()
cake_length = int(cake_length)
vertical_cut = int(vertical_cut)
horizontal_cut = int(horizontal_cut)

if(horizontal_cut < cake_length / 2.0):
    horizontal_cut = cake_length - horizontal_cut

if vertical_cut < cake_length / 2.0:
    vertical_cut = cake_length - vertical_cut

print(horizontal_cut * vertical_cut * 4)
