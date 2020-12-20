#Not Done

cake_width = int(input())
num_pieces = int(input())
area = 0

for i in range(num_pieces):
    piece_dimensions = input().split()
    area += int(piece_dimensions[0]) * int(piece_dimensions[1])

print(area // cake_width)
