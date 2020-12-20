def get_letter_val(current_letter):
    if current_letter == ' ':
        return 0
    elif current_letter == "'":
        return 1

    return ord(current_letter) - ord('A') + 2


def get_best_path(first_val, second_val):
    if abs(second_val - first_val) <= 14:
        return abs(second_val - first_val)

    total = 0
    if second_val < 14:
        total += second_val
        total += 28 - first_val
    else:
        total += first_val
        total += 28 - second_val

    return total


total_drills = int(input())

for drill in range(total_drills):
    racing_key = input()
    total_feet = 0
    for index in range(1, len(racing_key)):
        past_letter = racing_key[index - 1]
        current_letter = racing_key[index]

        numeric_of_past = get_letter_val(past_letter)
        numeric_of_current = get_letter_val(current_letter)
        total_chars = get_best_path(numeric_of_past, numeric_of_current)
        total_feet += total_chars * (60 / 28)

    total_time = total_feet / 15
    total_time += len(racing_key)

    print(total_time)
