words = input()
new_word = ""
counter = 0
vowels = ['a', 'e', 'i', 'o', 'u']

while counter < len(words):
    new_word += words[counter]
    if words[counter] in vowels:
        counter += 2
    counter += 1

print(new_word)
