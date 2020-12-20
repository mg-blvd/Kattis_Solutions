def check_decr(starter, sets):
    for i in range(sets - 2):
        new_name = input()
        if starter < new_name:
            print("NEITHER")
            return
        starter = new_name
    print("DECREASING")

def chec_incr(starter, sets):
    for i in range(sets - 2):
        new_name = input()
        if new_name < starter:
            print("NEITHER")
            return
        starter = new_name
    print("INCREASING")

sets = int(input())
first_name = input()
second_name = input()

if first_name > second_name:
    check_decr(second_name, sets)
else:
    chec_incr(second_name, sets)
