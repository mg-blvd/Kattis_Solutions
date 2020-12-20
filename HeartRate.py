times = int(input())

for i in range(times):
    beats, time = input().split()
    beats = float(beats)
    time = float(time)
    t = 60 / time
    bpm = 60 * beats / time
    print("{0:.4f}".format(bpm - t),"{0:.4f}".format(bpm), "{0:.4f}".format(bpm + t))
