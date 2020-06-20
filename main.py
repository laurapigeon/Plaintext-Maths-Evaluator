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


def get_object_list(string):
    current_type = None
    object_list = list()
    current_num = list()
    current_op = list()
    for i, char in enumerate(string):
        if char in m.NUMBERS:
            if current_type == "op":
                current_op = "".join(current_op)
                object_list.append([current_op, "c"])
                current_op = list()
            current_type = "num"
            current_num.append(char)
        else:
            if current_type == "num":
                current_num = "".join(current_num)
                object_list.append([current_num, "n"])
                current_num = list()
            current_type = "op"
            current_op.append(char)

    if current_type == "op":
        current_op = "".join(current_op)
        object_list.append([current_op, "c"])
    elif current_type == "num":
        current_num = "".join(current_num)
        object_list.append([current_num, "n"])

    return object_list


def sort_object_list(object_list):
    for i, object_info in enumerate(object_list):
        if object_info[1] == "n" and "," in object_info[0]:
            object_list[i][0] = object_info[0].split(",")

            for number in object_info[0]:
                if number.count(".") > 1:
                    print("Invalid number {}".format(number))
                    quit()

        elif object_info[1] == "c":
            op_list = split_op_string(object_info[0])

            insert_list = list()
            for j, operation in enumerate(op_list):
                if get_operation_info(operation, 2) in (1, 3, 5) and (j == 0 or get_operation_info(op_list[j - 1], 2) in (1, 2)):
                    insert_list.append(["*", "o"])
                insert_list.append([operation, "o"])
            if get_operation_info(operation, 2) in (1, 2):
                insert_list.append(["*", "o"])

            object_list[i:i + 1] = insert_list

    return object_list


def split_op_string(op_string):
    global op_list

    op_list = list()

    valid = test_op_string(op_string)
    if valid:
        return op_list
    else:
        print("Invalid equation {}".format(op_string))
        quit()


def test_op_string(op_string):
    global op_list

    if op_string in m.OPERATOR_STRINGS:
        op_list.append(op_string)
        return True

    backup_op_string = op_string
    valid = False
    for i in range(len(op_string)):
        if op_string[0:i] in m.OPERATOR_STRINGS:
            op_list.append(op_string[0:i])
            op_string = op_string[i:len(op_string)]
            valid = test_op_string(op_string)

            if valid:
                break
            else:
                op_string = backup_op_string
                del op_list[len(op_list) - 1]

    return valid


def get_operation_info(string, info):
    index = m.OPERATOR_STRINGS.index(string)
    return m.OPERATORS[index][info]


done = False
while not done:
    string = tidy_string(input("Equation here:\n || "))
    print("tidied string input\n ||", string)
    start, end = get_substring_ends(string)
    substring = string[start:end + 1]
    print("found deepest substring\n ||", substring)
    object_list = get_object_list(substring[1:len(substring) - 1])
    object_list = sort_object_list(object_list)
    print("sequenced parts of substring and added asterisks\n ||", object_list)
    for x in object_list:
        print(x[0], end="")
    done = True
