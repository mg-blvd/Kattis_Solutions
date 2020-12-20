startTime, classStartTime, routeAmounts = input().split()
walkingTimes = input().split()
routeTime = input().split()
routeArrivalTimes = input().split()

classStartTime = int(classStartTime)
routeAmounts = int(routeAmounts)
startTime = int(startTime)
startTime += int(walkingTimes[0])

for i in range(int(routeAmounts)):

    waitingTime = startTime % int(routeArrivalTimes[i])
    if waitingTime != 0:
        startTime += int(routeArrivalTimes[i]) - waitingTime

    startTime += int(routeTime[i])
    startTime += int(walkingTimes[i + 1])

if(startTime <= int(classStartTime)):
    print('yes')
else:
    print('no')
