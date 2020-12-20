set_change, paul_points, opp_points = input().split()
total_points = int(paul_points) + int(opp_points)
set_change = int(set_change)

if (total_points // set_change) % 2 == 0:
    print('paul')
else:
    print('opponent')
