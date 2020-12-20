def check_dupl(word):
    for i in range(len(word)):
        found_space = word.find(word[i], i + 1)
        if found_space != -1:
            return 1
    return 0

curr_word = input()
print(check_dupl(curr_word))
