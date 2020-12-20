apax_name = input()
shortened_name = ""

for i in range(len(apax_name)):
    if i == 0:
        shortened_name += apax_name[i]
    else:
        if apax_name[i] != apax_name[i - 1]:
            shortened_name += apax_name[i]

print(shortened_name)
