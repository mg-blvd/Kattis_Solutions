teams = int(input())
schools = []

for i in range(teams):
    school, team = input().split()
    if school in schools:
        continue
    schools.append(school)
    print(f"{school} {team}")
    if len(schools) == 12:
        break
