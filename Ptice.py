Adrian = ["A", "B", "C"]
Bruno = ["B", "A", "B", "C"]
Goran = ["C", "C", "A", "A", "B", "B"]

questions = int(input())
answers = input()

correct_ans = [0, 0, 0]

a_pos = 0
b_pos = 0
g_pos = 0

for i in answers:
    if i == Adrian[a_pos]:
        correct_ans[0] += 1
    if i == Bruno[b_pos]:
        correct_ans[1] += 1
    if i == Goran[g_pos]:
        correct_ans[2] += 1

    a_pos += 1
    b_pos += 1
    g_pos += 1

    if a_pos == 3:
        a_pos = 0
    if b_pos == 4:
        b_pos = 0
    if g_pos == 6:
        g_pos = 0

most_correct = max(correct_ans)
print(most_correct)

if most_correct == correct_ans[0]:
    print("Adrian")
if most_correct == correct_ans[1]:
    print("Bruno")
if most_correct == correct_ans[2]:
    print("Goran")
