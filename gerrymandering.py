import math

precints, disctricts = input().split()
districtInfo = []
votesTotal = 0
totalAWasted = 0
totalBWasted = 0

for i in range(int(disctricts)):
    districtInfo.append({'a': 0, 'b': 0})

for i in range(int(precints)):
    district, aVotes, bVotes = input().split()
    aVotes = int(aVotes)
    bVotes = int(bVotes)
    district = int(district) - 1
    votesTotal += aVotes + bVotes
    districtInfo[district]['a'] += aVotes
    districtInfo[district]['b'] += bVotes

for district in districtInfo:
    bWasted = 0
    aWasted = 0
    totalVoted = district['a'] + district['b']
    minimumWinning = math.floor(totalVoted / 2) + 1

    if(district['a'] > district['b']):
        bWasted = district['b']
        aWasted = district['a'] - minimumWinning
        print("A", end=' ')
    else:
        bWasted = district['b'] - minimumWinning
        aWasted = district['a']
        print("B", end=' ')

    print(aWasted, bWasted)
    totalAWasted += aWasted
    totalBWasted += bWasted

print((abs(totalAWasted - totalBWasted)) / votesTotal)
