import math_functions as m
import re
import discord
import logging


intents = discord.Intents.default()  # Create a default intents object
intents.typing = False  # Disable the typing events, if desired
intents.presences = True  # Disable the presence events, if desired
intents.message_content = True

client = discord.Client(intents=intents)
logging.basicConfig()


class Evaluate:
    def tidy_string(string):
        string = re.sub(" ", "", string)
        string = re.sub("\\\\", "", string)
        if PRINT_STEPS:
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
        if PRINT_STEPS:
            print("removed {} out of place open brackets".format(layer))

        for i, bracket in enumerate(bracket_remove):
            del characters[bracket - i]
        if PRINT_STEPS:
            print("removed {} out of place close brackets".format(len(bracket_remove)))

        asterix_add = list()
        prev_char = None
        for i, char in enumerate(characters):
            if char in m.BRACKETS[0] and (prev_char in m.BRACKETS[1] or prev_char in m.NUMBERS) or (prev_char in m.BRACKETS[1] and char in m.NUMBERS):
                asterix_add.append(i)
            prev_char = char

        for i, asterix in enumerate(asterix_add):
            characters.insert(asterix + i, "*")
        if PRINT_STEPS:
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

    def sort_object_list(object_list, loop):
        for i, object_info in enumerate(object_list):
            if object_info[1] == "n":
                if "," in object_info[0]:
                    object_list[i][0] = object_info[0].split(",")

                    for number in object_info[0]:
                        if number.count(".") > 1:
                            if loop > 0:
                                raise Exception("Invalid number {}".format(number))
                            else:
                                raise Exception(None)

                elif object_info[0].count(".") > 1:
                    if loop > 0:
                        raise Exception("Invalid number {}".format(object_info[0]))
                    else:
                        raise Exception(None)

            elif object_info[1] == "c":
                op_list = Evaluate.split_op_string(object_info[0], loop)

                insert_list = list()
                prev_type = None
                for j, operation in enumerate(op_list):
                    operation_type = Evaluate.get_operation_info(operation, 2)
                    if operation == "-" and ((not j and i) or prev_type in (1, 2)):
                        insert_list.append(["+", "o", 104])
                    elif operation_type in (1, 3, 5) and ((not j and i) or prev_type in (1, 2)):
                        insert_list.append(["*", "o", 103])
                    insert_list.append([operation, "o", Evaluate.get_operation_info(operation, "index")])
                    prev_type = operation_type

                if operation_type in (1, 2) and i != len(object_list) - 1:
                    insert_list.append(["*", "o", 103])

                object_list[i:i + 1] = insert_list

        return object_list

    def split_op_string(op_string, loop):
        op_list = list()

        valid = Evaluate.test_op_string(op_string, op_list)
        if valid:
            return op_list
        elif loop > 0:
            raise Exception("Invalid equation {}".format(op_string))
        else:
            raise Exception(None)

    def test_op_string(op_string, op_list):
        if op_string in m.OPERATOR_STRINGS:
            op_list.append(op_string)
            return True

        backup_op_string = op_string
        valid = False
        for i in range(len(op_string)):
            if op_string[0:i] in m.OPERATOR_STRINGS:
                op_list.append(op_string[0:i])
                op_string = op_string[i:len(op_string)]
                valid = Evaluate.test_op_string(op_string, op_list)

                if valid:
                    break
                else:
                    op_string = backup_op_string
                    del op_list[len(op_list) - 1]

        return valid

    def evaluate_object_list(object_list):
        done = False
        while not done:
            min_priority = len(m.OPERATOR_STRINGS) + 1
            index = None
            for i, object_info in enumerate(object_list):
                if len(object_info) == 3:
                    if object_info[2] < min_priority:
                        min_priority = object_info[2]
                        index = i

            if index is not None:
                Evaluate.evaluate_object(index, object_list)

            if len(object_list) == 1:
                done = True

        return str(object_list[0][0])

    def evaluate_object(i, object_list):
        has_a = m.OPERATORS[object_list[i][2]][2] in (2, 4)
        has_b = m.OPERATORS[object_list[i][2]][2] in (3, 4)
        has_list_b = m.OPERATORS[object_list[i][2]][2] == 5

        if has_a:
            if i != 0:
                if object_list[i - 1][1] == "o":
                    if m.OPERATORS[object_list[i - 1][2]][2] not in (3, 4, 5):
                        Evaluate.evaluate_object(i - 1, object_list)
                    else:
                        raise Exception("Recursive operation {}{}".format(object_list[i - 1][0], object_list[i][0]))
            else:
                raise Exception("Operation {} references edge of expression".format(object_list[i][0]))

            a = float(object_list[i - 1][0])
        else:
            a = 0.0
        if has_b:
            if i != len(object_list) - 1:
                if object_list[i + 1][1] == "o":
                    if m.OPERATORS[object_list[i + 1][2]][2] not in (2, 4):
                        Evaluate.evaluate_object(i + 1, object_list)
                    else:
                        raise Exception("Recursive operation {}{}".format(object_list[i][0], object_list[i + 1][0]))
            else:
                raise Exception("Operation {} references edge of expression".format(object_list[i][0]))

            b = float(object_list[i + 1][0])
        elif has_list_b:
            b = [float(x) for x in object_list[i + 1][0]]
        else:
            b = 0.0

        output = m.OPERATORS[object_list[i][2]][1](a, b)

        lower_bound = (i, i - 1)[has_a]
        upper_bound = (i + 1, i + 2)[has_b or has_list_b]
        object_list[lower_bound:upper_bound] = [[output, "n"]]

    def get_operation_info(string, info):
        index = m.OPERATOR_STRINGS.index(string)
        if info == "index":
            return index
        else:
            return m.OPERATORS[index][info]

    def main(string_input):
        string = Evaluate.tidy_string(string_input)
        if PRINT_STEPS:
            print(" ||", string)

        done = False
        loop = 0
        while not done:
            substring_ends = Evaluate.get_substring_ends(string)
            if substring_ends is None:
                done = True
                break

            substring = string[substring_ends[0]:substring_ends[1] + 1]
            if PRINT_STEPS:
                print("found deepest substring\n ||", substring)

            object_list = Evaluate.get_object_list(substring[1:len(substring) - 1])
            object_list = Evaluate.sort_object_list(object_list, loop)
            if PRINT_STEPS:
                print("sequenced parts of substring and added asterisks\n ||", object_list)
                print(" || ", end="")
                for x in object_list:
                    print(x[0], end="")
                print("")

            result = Evaluate.evaluate_object_list(object_list)
            if PRINT_STEPS:
                print("evaluated substring to equal {}".format(result))

            temp_list = list(string)
            temp_list[substring_ends[0]:substring_ends[1] + 1] = result
            string = "".join(temp_list)
            if PRINT_STEPS:
                print("placed result into equation\n ||", string)

            loop += 1

        output = string
        if output not in ("False", "True"):
            output = float(output)
            if output == int(output):
                output = int(output)
        return str(output)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    channel = client.get_channel(CHANNEL_ID)

    # Check if the channel is valid
    if channel is not None:
        # Send a test message
        await channel.send("Bot is ready and can send messages!")
    else:
        print("Invalid channel ID")


@client.event
async def on_message(message):
    global current_num
    global high_score
    global prev_user
    global singleplayer

    if message.channel.id != CHANNEL_ID:
        return

    if message.author == client.user:
        return

    if message.content.startswith("c!help"):
        await message.channel.send("Type equations and the bot will try to evaluate them! 'c!operations' for a list of operations, 'c!server' for the high score")

    elif message.content.startswith("c!commands"):
        await message.channel.send("'c!help' for help\n'c!operations' for a list of operations\n'c!mode' to change the mode\n'c!server' for the high score\n'c!singleplayer' to toggle singleplayer")

    elif message.content.startswith("c!operations"):
        await message.channel.send(", ".join(m.OPERATOR_STRINGS))

    elif message.content.startswith("c!singleplayer"):
        singleplayer = not singleplayer
        await message.channel.send("Turned singleplayer {}".format(("off", "on")[singleplayer]))

    elif message.content.startswith("c!mode"):
        if message.content.endswith("count"):
            current_num = int(open("score_store.txt", "r").read().split(" ")[0])
            high_score = int(open("score_store.txt", "r").read().split(" ")[1])
            prev_user = None
            await message.channel.send("Mode changed to counter, next number is {}".format(current_num + 1))
        elif message.content.endswith("eval"):
            open("score_store.txt", "w").write(" ".join((str(current_num), str(high_score))))
            current_num = None
            await message.channel.send("Mode changed to evaluater")
        else:
            await message.channel.send("Current mode is {}. 'c!mode count' for counter, 'c!mode eval' for evaluater".format(("counter", "evaluater")[current_num is None]))

    elif set(message.content) <= m.CHAR_SET:
        try:
            output = Evaluate.main(message.content)
            if current_num is None:
                await message.channel.send(output)
            else:
                if message.author != prev_user or singleplayer:
                    if round(float(output)) == current_num + 1:
                        if current_num + 1 > high_score:
                            await message.add_reaction("☑️")
                        else:
                            await message.add_reaction("✅")
                        current_num += 1
                        prev_user = message.author
                        open("score_store.txt", "w").write(" ".join((str(current_num), str(high_score))))
                    else:
                        if current_num > BASE_NUM:
                            await message.add_reaction("❌")
                            await message.channel.send("{} RUINED IT AT **{}**!! Next number is **1**. Wrong number.".format(message.author.mention, current_num))
                            if current_num > high_score:
                                high_score = current_num
                            current_num = BASE_NUM
                            prev_user = None
                            open("score_store.txt", "w").write(" ".join((str(current_num), str(high_score))))
                        else:
                            await message.add_reaction("⚠️")
                            await message.channel.send("Incorrect number! Next number is **1**. No scores have been changed since the current number was 0.")
                            prev_user = None
                else:
                    await message.add_reaction("❌")
                    await message.channel.send("{} RUINED IT AT **{}**!! Next number is **1**. You can't count two numbers in a row.".format(message.author.mention, current_num))
                    if current_num > high_score:
                        high_score = current_num
                    current_num = BASE_NUM
                    prev_user = None
                    open("score_store.txt", "w").write(" ".join((str(current_num), str(high_score))))

        except Exception as error_text:
            if str(error_text) != "None" and SEND_ERROR_MESSAGES:
                await message.channel.send(error_text)
            else:
                print(error_text)

PRINT_STEPS = True
SEND_ERROR_MESSAGES = False
DISCORD = True
BASE_NUM = 0
CHANNEL_ID = 724602804777254986
BOT_TOKEN = ""
singleplayer = False
current_num = int(open("score_store.txt", "r").read().split(" ")[0])
high_score = int(open("score_store.txt", "r").read().split(" ")[1])
prev_user = None

if DISCORD:
    client.run(BOT_TOKEN)
else:
    while True:
        print(Evaluate.main(input("Equation here:\n")))
