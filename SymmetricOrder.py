def get_words(number):
    words = []
    for i in range(number):
        words.append(input())
    return words

def get_order(words):
    new_order = []
    for i in range(len(words) - 1, -1, -1):
        if i % 2 == 1:
            new_order.append(words[i])
        else:
            new_order = [words[i]] + new_order
    return new_order

def display(set_num, words):
    print(f"SET {set_num}")
    for i in words:
        print(i)

num_lines = int(input())
counter = 0

while num_lines != 0:
    counter += 1
    words = get_words(num_lines)
    display_order = get_order(words)
    display(counter, display_order)
    num_lines = int(input())
