whitespaces = 0
uppers = 0
lowers = 0
characters = 0
words = input()

for letter in words:
    if letter == '_':
        whitespaces += 1
    elif letter.isupper():
        uppers += 1
    elif letter.islower():
        lowers += 1
    else:
        characters += 1

print(whitespaces / len(words))
print(lowers / len(words))
print(uppers / len(words))
print(characters / len(words))
