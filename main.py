import math_functions as m
import re


def tidy_string(string):
    string = re.sub(' ', '', string)
    print("removed spaces")

    characters = list(string)
    bracket_remove = list()
    bracket_start = list()
    layer = 0
    for i, char in enumerate(characters):
        if char in m.BRACKETS[0]:
            bracket_start.append(i)
            layer += 1

        if char in m.BRACKETS[1]:
            if layer == 0:
                bracket_remove.append(i)
            else:
                layer -= 1

    for i in range(layer):
        del characters[bracket_start[-1 - i]]
    print("removed {} out of place open brackets".format(layer))

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

    characters.insert(0, "(")
    characters.append(")")

    return "".join(characters)


def get_substring_ends(string):
    bracket_start = None
    bracket_end = None
    for i, char in enumerate(string):
        if char in m.BRACKETS[0]:
            bracket_start = i

        if char in m.BRACKETS[1]:
            bracket_end = i
            break

    return bracket_start, bracket_end


def get_nums_and_ops(string):
    current_type = None
    numbers = list()
    current_num = list()
    operators = list()
    current_op = list()
    for i, char in enumerate(string):
        if char in m.NUMBERS:
            if current_type == "op":
                current_op = "".join(current_op)
                if current_op in m.OPERATOR_STRINGS:
                    operators.append(current_op)
                    current_op = list()
                else:
                    for operator_string in m.OPERATOR_STRINGS:
                        if operator_string in current_op:
                            pass  # GIVE A CHANCE FOR 5!+e*5 ETC
                    print("Operator {} not found".format(current_op))  # THROW ERROR
                    quit()
            current_type = "num"
            current_num.append(char)
        else:
            if current_type == "num":
                current_num = "".join(current_num)
                if current_num.count(".") < 1 or current_num.count(",") > 0:
                    numbers.append(current_num)
                    current_num = list()
                else:
                    print("Number {} invalid".format(current_num))  # THROW ERROR
                    quit()
            current_type = "op"
            current_op.append(char)

    if current_type == "op":
        current_op = "".join(current_op)
        if current_op in m.OPERATOR_STRINGS:
            operators.append(current_op)
        else:
            print("Operator {} not found".format(current_op))  # THROW ERROR
            quit()
    if current_type == "num":
        current_num = "".join(current_num)
        if current_num.count(".") < 1 or current_num.count(",") > 0:
            numbers.append(current_num)
        else:
            print("Number {} invalid".format(current_num))  # THROW ERROR
            quit()

    return numbers, operators


done = False
while not done:
    string = tidy_string(input())
    start, end = get_substring_ends(string)

    substring = string[start:end + 1]
    print(substring)
    numbers, operations = get_nums_and_ops(substring[1:len(substring) - 1])
    print(numbers, operations)
    done = True
