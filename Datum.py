import sys
day, month = input().split()
month = int(month)
day = int(day)

for i in range(month - 1):
    if (i == 0) or (i == 2) or (i == 4) or (i == 6) or (i == 7) or  (i == 9) or (i == 11):
        day += 31
    elif i == 1:
        day += 28
    else:
        day += 30
if day % 7 == 1:
    print("Thursday")
elif day % 7 == 2:
    print("Friday")
elif day % 7 == 3:
    print("Saturday")
elif day % 7 == 4:
    print("Sunday")
elif day % 7 == 5:
    print("Monday")
elif day % 7 == 6:
    print("Tuesday")
else:
    print("Wednesday")
