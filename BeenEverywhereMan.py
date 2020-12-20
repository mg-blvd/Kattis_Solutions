import sys
times = int(input())

for i in range(times):
    counter = 0
    cities = []
    trips = int(input())
    for j in range(trips):
        city = input()
        if city not in cities:
            cities.append(city)
            counter += 1
    print(counter)
