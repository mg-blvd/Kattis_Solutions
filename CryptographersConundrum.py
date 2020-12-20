current_combo = input()

matches = 0
word_len = int(len(current_combo))
for i in range(0, word_len, 3):
    if current_combo[i] == 'P':
        matches += 1
    if i + 1 < word_len:
        if current_combo[i + 1] == 'E':
            matches += 1
    if i + 2 < word_len:
        if current_combo[i + 2] == 'R':
            matches += 1

print(word_len - matches)
