from math import pi

pizza_rad, crust_rad = input().split()
cheese_rad = int(pizza_rad) - int(crust_rad)

print((cheese_rad ** 2) / (int(pizza_rad) ** 2) * 100)
