import math_functions as m
import re


def tidy_string(string):
    string = re.sub(' ', '', string)
    print("removed spaces")

    characters = list(string)

    bracket_remove = list()
    layer = 0
    for i, char in enumerate(characters):
        if char in m.BRACKETS[0]:
            layer += 1

        if char in m.BRACKETS[1]:
            if layer == 0:
                bracket_remove.append(i)
            else:
                layer -= 1

    for _ in range(layer):
        characters.append(")")
    print("added {} close brackets".format(layer))

    for i, bracket in enumerate(bracket_remove):
        del characters[bracket - i]
    print("removed {} out of place close brackets".format(len(bracket_remove)))

    asterix_add = list()
    prev_char = None
    for i, char in enumerate(characters):
        if char in m.BRACKETS[0] and (prev_char in m.BRACKETS[1] or prev_char in m.NUMBERS) or (prev_char in m.BRACKETS[1] and char in m.NUMBERS):
            asterix_add.append(i)
        prev_char = char

    for i, asterix in enumerate(asterix_add):
        characters.insert(asterix + i, "*")
    print("inserted {} missing asterixes".format(len(asterix_add)))

    return "".join(characters)


while True:
    print()
    print(tidy_string(input()))

"""
bracket_start = list()
bracket_end = list()
for char, i in enumerate(characters):
    if char in m.BRACKETS[0]:
        bracket_start.append(i)
        layer += 1

    if char in m.BRACKETS[1]:
        bracket_end.append(i)
        layer -= 1


done = False
while not done:
    bracket_start = None
    bracket_end = None
    for char, i in enumerate(string):
        if char in m.BRACKETS[0]:
            bracket_start = i

        if char in m.BRACKETS[1]:
            bracket_end = i
            break
"""