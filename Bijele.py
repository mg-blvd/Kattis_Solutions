correct_piece_count = [1, 1, 2, 2, 2, 8]

piece_count = input().split()

set_changes = ""
for i in range(len(piece_count)):
    set_changes += str(correct_piece_count[i] - int(piece_count[i]))
    if i != len(piece_count) - 1:
        set_changes += " "

print(set_changes)
