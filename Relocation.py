num_companies, queries = input().split()
company_location = input().split()

for i in range(int(num_companies)):
    company_location[i] = int(company_location[i])

for i in range(int(queries)):
    command = input().split()

    if command[0] == '1':
        company_location[int(command[1]) - 1] = int(command[2])

    else:
        first_location = int(command[1]) - 1
        second_location = int(command[2]) - 1

        print(abs(company_location[first_location] -
                  company_location[second_location]))
