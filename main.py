import math_functions as m
import re


def tidy_string(string):
    string = re.sub(' ', '', string)
    if print_steps:
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
    if print_steps:
        print("removed {} out of place open brackets".format(layer))

    for i, bracket in enumerate(bracket_remove):
        del characters[bracket - i]
    if print_steps:
        print("removed {} out of place close brackets".format(len(bracket_remove)))

    asterix_add = list()
    prev_char = None
    for i, char in enumerate(characters):
        if char in m.BRACKETS[0] and (prev_char in m.BRACKETS[1] or prev_char in m.NUMBERS) or (prev_char in m.BRACKETS[1] and char in m.NUMBERS):
            asterix_add.append(i)
        prev_char = char

    for i, asterix in enumerate(asterix_add):
        characters.insert(asterix + i, "*")
    if print_steps:
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
            return (bracket_start, bracket_end)

    return None


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
                    quit()  # CHECK NON LISTS

        elif object_info[1] == "c":
            op_list = split_op_string(object_info[0])

            insert_list = list()
            prev_type = None
            for j, operation in enumerate(op_list):
                operation_type = get_operation_info(operation, 2)
                if operation == "-" and ((not j and i) or prev_type in (1, 2)):
                    insert_list.append(["+", "o", 104])
                elif operation_type in (1, 3, 5) and ((not j and i) or prev_type in (1, 2)):
                    insert_list.append(["*", "o", 103])
                insert_list.append([operation, "o", get_operation_info(operation, "index")])
                prev_type = operation_type

            if operation_type in (1, 2):
                insert_list.append(["*", "o", 103])

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


def evaluate_object_list(object_list):
    while len(object_list) > 1:
        min_priority = len(m.OPERATOR_STRINGS) + 1
        index = None
        for i, object_info in enumerate(object_list):
            if len(object_info) == 3:
                if object_info[2] < min_priority:
                    min_priority = object_info[2]
                    index = i

        evaluate_object(index)

    return str(object_list[0][0])


def evaluate_object(i):
    global object_list

    has_a = m.OPERATORS[object_list[i][2]][2] in (2, 4)
    has_b = m.OPERATORS[object_list[i][2]][2] in (3, 4, 5)
    has_snazzy_b = m.OPERATORS[object_list[i][2]][2] == 5

    if object_list[i - 1][1] == "o" and has_a:
        evaluate_object(i - 1)
    elif object_list[i + 1][1] == "o" and has_b:
        evaluate_object(i + 1)
    else:
        a = float(("0", object_list[i - 1][0])[has_a])
        b = ("0", object_list[i + 1][0])[has_b]
        if has_snazzy_b:
            b = [int(x) for x in list(b)]
        else:
            b = float(b)
        output = m.OPERATORS[object_list[i][2]][1](a, b)
        lower_bound = (i, i - 1)[has_a]
        upper_bound = (i + 1, i + 2)[has_b]
        object_list[lower_bound:upper_bound] = [[output, "n"]]


def get_operation_info(string, info):
    index = m.OPERATOR_STRINGS.index(string)
    if info == "index":
        return index
    else:
        return m.OPERATORS[index][info]


print_steps = False

while True:
    string = tidy_string(input("Equation here:\n || "))
    if print_steps:
        print(" ||", string)

    done = False
    while not done:
        substring_ends = get_substring_ends(string)
        if substring_ends is None:
            done = True
            break
        substring = string[substring_ends[0]:substring_ends[1] + 1]
        if print_steps:
            print("found deepest substring\n ||", substring)
        object_list = get_object_list(substring[1:len(substring) - 1])
        object_list = sort_object_list(object_list)
        if print_steps:
            print("sequenced parts of substring and added asterisks\n ||", object_list)
            print(" || ", end="")
            for x in object_list:
                print(x[0], end="")
            print("")
        result = evaluate_object_list(object_list)
        if print_steps:
            print("evaluated substring to equal {}".format(result))
        temp_list = list(string)
        temp_list[substring_ends[0]:substring_ends[1] + 1] = result
        string = "".join(temp_list)
        if print_steps:
            print("placed result into equation\n ||", string)

    print("RESULT:", string, "\n--------\n")