from math import ceil, sin, radians

height, angle = input().split()

side_length = int(height) / sin(radians(int(angle)))
print(ceil(side_length))
