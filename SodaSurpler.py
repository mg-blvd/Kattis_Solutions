import math

cans, found_cans, cans_price = input().split()
cans = int(cans) + int(found_cans)
cans_price = int(cans_price)
total_sodas = 0

while cans >= cans_price:
    bought_cans = math.floor(cans / cans_price)
    total_sodas += bought_cans
    cans = bought_cans + (cans % cans_price)

print(total_sodas)
