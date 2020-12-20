morse_symbols = [[], ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '..--', '.-.-', '---.', '----']]
for i in range(26):
    morse_symbols[0].append(chr(i + 65))

new_chars = ['_', ',', '.', '?']
for i in range(4):
    morse_symbols[0].append(new_chars[i])

def change_val(a):
    a = 5

b = 6
change_val(b)
print(b)
