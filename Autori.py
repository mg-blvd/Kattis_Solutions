import sys

name = input()
new_name = ""

for i in name:
    if i.isupper():
        new_name = new_name + i
print(new_name)
