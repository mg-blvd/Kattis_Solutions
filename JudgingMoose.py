tines = input().split()
for i in range(2):
    tines[i] = int(tines[i])

tines.sort()

if tines == [0, 0]:
    print("Not a moose")
elif tines[0] == tines[1]:
    print(f"Even {tines[0] * 2}")
else:
    print(f"Odd {tines[1] * 2}")
