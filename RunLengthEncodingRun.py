def decode(phrase):
    new_message = ''
    for i in range(len(phrase) // 2):
        new_message += phrase[i * 2] * int(phrase[i * 2 + 1])
    print(new_message)

def encode(phrase):
    new_message = ''
    cur_index = 1
    counter = 1
    cur_char = phrase[0]
    while cur_index < len(phrase):
        if cur_char == phrase[cur_index]:
            counter += 1
        else:
            new_message += cur_char + str(counter)
            counter = 1
            cur_char = phrase[cur_index]
        cur_index += 1
    new_message += cur_char + str(counter)
    print(new_message)

inputs = input().split()
if inputs[0] == 'D':
    decode(inputs[1])
else:
    encode(inputs[1])
