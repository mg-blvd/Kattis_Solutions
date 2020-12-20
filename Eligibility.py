sets = int(input())

for i in range(sets):
    person = input().split()
    print(person[0], end=' ')
    if int(person[1][:4]) >= 2010:
        print('eligible')
    elif int(person[2][:4]) >= 1991:
        print('eligible')
    elif int(person[-1]) >= 41:
        print('ineligible')
    else:
        print('coach petitions')
