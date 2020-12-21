num_lines = int(input())

for case in range(num_lines):
    devices = 0
    strips = input().split()
    if(strips[0] == 0):
        devices = 1
    else:
        for strip_index in range(1, len(strips)):
            devices += int(strips[strip_index]) - 1
            if strip_index == len(strips) - 1:
                devices += 1
    print(devices)
