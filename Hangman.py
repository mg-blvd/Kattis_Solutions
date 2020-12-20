word = input()
word = "".join(set(word))
letter_order = input()
solved = False
counter = 0
losing = 0

for i in range(26):
    if letter_order[i] in word:
        counter += 1
        if counter == len(word):
            print("WIN")
            solved = True
            break
    else:
        losing += 1
        if losing == 10:
            print("LOSE")
            break
