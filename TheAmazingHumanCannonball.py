from math import cos, sin, radians, pow

def find_time(distance, angle, velocity):
    divisor = velocity * cos(radians(angle))
    return distance / divisor

def find_height(velocity, time, angle):
    lhs = velocity * time * sin(radians(angle))
    rhs = pow(time, 2) * 9.81 / 2
    return lhs - rhs

sets = int(input())

for i in range(sets):
    v, angle, h_distance, height1, height2 = input().split()
    dude_height = find_height(float(v), find_time(float(h_distance), float(angle), float(v)), float(angle))
    if float(height1) + 1 <= dude_height <= float(height2) - 1:
        print("Safe")
    else:
        print("Not Safe")
