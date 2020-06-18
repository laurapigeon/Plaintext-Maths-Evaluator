import math_functions as m
import re

string = "3 + (5-2) * 4"

string = re.sub(' ', '', string)

characters = list(string)
layer = 0

bracket_remove = list()
for char, i in enumerate(characters):
    if char in m.BRACKETS[1]:
        if layer == 0:
            bracket_remove.append(i)

for bracket, i in enumerate(bracket_remove):
    del characters[bracket - i]

asterix_add = list()
prev_char = None
for char, i in enumerate(characters):
    if char in m.BRACKETS[0] and prev_char in m.BRACKETS[1]:
        asterix_add.append(i)
    prev_char = char

for asterix, i in enumerate(bracasterix_addket_remove):
    characters.insert(bracket + i, "*")

bracket_start = list()
bracket_end = list()
for char, i in enumerate(characters):
    if char in m.BRACKETS[0]:
        bracket_start.append(i)
        layer += 1

    if char in m.BRACKETS[1]:
        bracket_end = i
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
