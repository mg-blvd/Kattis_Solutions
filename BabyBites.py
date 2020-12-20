num_bites = int(input())
sequence = input().split()
phrase = 'makes sense'

for i in range(num_bites):
    if sequence[i] != 'mumble' and int(sequence[i]) != i + 1:
        phrase = 'something is fishy'
        break

print(phrase)
