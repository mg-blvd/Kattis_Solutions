number = int(input())
a_amount = 0
b_amount = 0

a_amount = 1

for i in range(0, number):
    new_b = b_amount + a_amount
    a_amount = b_amount
    b_amount = new_b

print(a_amount, b_amount)
