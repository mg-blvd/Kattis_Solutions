phrase = input().split()
result = "yes"

for i in range(len(phrase) - 1):
    for y in range(i + 1, len(phrase)):
        if phrase[i] == phrase[y]:
            result = "no"
            break

print(result)
