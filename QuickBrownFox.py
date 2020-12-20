sets = int(input())

for y in range(sets):
    letters = []
    for i in range(26):
        letters.append(False)

    phrase = input()

    for char in phrase:
        if char.isalpha():
            letters[ord(char.lower()) - 97] = True

    if False not in letters:
        print('pangram')
    else:
        print('missing ', end = '')
        for i in range(26):
            if letters[i] == False:
                print(chr(i + 97), end='')
        print('\n')
