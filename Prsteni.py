from fractions import Fraction

num_rings = int(input())
ring_sizes = input().split()
first_ring = int(ring_sizes[0])

for i in range(1, len(ring_sizes)):
    if first_ring % int(ring_sizes[i]) == 0:
        print(str(first_ring // int(ring_sizes[i])) + "/1")
    else:
        print(Fraction(first_ring / int(ring_sizes[i])))
