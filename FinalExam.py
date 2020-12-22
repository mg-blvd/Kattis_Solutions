prob_amount = int(input())
last_answer = ''
cur_answer = ''
score = 0

for problem in range(prob_amount):
    if problem == 0:
        last_answer = input()
        continue
    cur_answer = input()
    if cur_answer == last_answer:
        score += 1
    last_answer = cur_answer

print(score)
