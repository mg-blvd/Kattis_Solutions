import sys
years, months = input().split()
years = int(years)
months = int(months)
past_years = input().split()
found = False

for i in range(len(past_years)):
    if months >= int(past_years[i]):
        print(f'It hadn\'t snowed this early in {i} years!')
        found = True
        break

if not found:
    print("It had never snowed this early!")
