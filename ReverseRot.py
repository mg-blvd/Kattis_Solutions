default_rot = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
def rotate_word(places, words):
    new_word = ""
    for i in range(len(message)):
        position = default_rot.find(words[i])
        if position + places < len(default_rot):
            new_pos = position + places
        else:
            new_pos = position + places - len(default_rot)
        new_word += default_rot[new_pos]
    return new_word[::-1]

line = input()
while line != '0':
    rot_places, message = line.split()
    rot_places = int(rot_places)
    print(rotate_word(rot_places, message))
    line = input()
