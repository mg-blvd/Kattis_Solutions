time = 0
person = int(input())
sets = int(input())
printed = False

for i in range(sets):
    vals = input().split()
    time += int(vals[0])
    if time >= 210:
        print(person)
        printed = True
        break
    if vals[1] == 'T':
        person += 1
        if person == 9:
            person = 1

if printed == False:
    print(person)
