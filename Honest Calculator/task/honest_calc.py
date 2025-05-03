# # Stage 1
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
#
# while True:
#     print(msg_0)
#     calc = input().split(" ")
#     # print(calc)
#     x = calc[0]
#     operation = calc[1]
#     y = calc[2]
#
#     try:
#         float(x)
#         float(y)
#     except ValueError:
#         print(msg_1)
#         continue
#     else:
#         if operation not in ["+", "-", "*", "/"]:
#             print(msg_2)
#             continue
#     break
#
# # End of Stage 1


# # Stage 2
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
#
# while True:
#     print(msg_0)
#     calc = input().split(" ")
#     # print(calc)
#     x = calc[0]
#     operation = calc[1]
#     y = calc[2]
#
#     try:
#         float(x)
#         float(y)
#     except ValueError:
#         print(msg_1)
#         continue
#     else:
#         if operation not in ["+", "-", "*", "/"]:
#             print(msg_2)
#             continue
#         elif operation == "/" and float(y) == 0:
#             print(msg_3)
#             continue
#     break
#
# result = 0.0
#
# if operation == "+":
#     result = float(x) + float(y)
# elif operation == "-":
#     result = float(x) - float(y)
# elif operation == "*":
#     result = float(x) * float(y)
# elif operation == "/":
#     result = float(x) / float(y)
#
# print(result)
#
# # End of Stage 2


# # Stage 3
# import sys
#
# # List of input and warning/error messages.
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
#
#
# # Variable for storing the result of a correct equation.
# memory = 0.0
#
# # Main loop. It loops until the user chooses 'n = no'. Decision-making is done in the inner loop at the end.
# while True:
#     # Loop for checking correct operands and operator.
#     while True:
#         print(msg_0)
#         calc = input().split(" ")
#         # print(calc)
#         x = calc[0]
#         operation = calc[1]
#         y = calc[2]
#
#         # Check if any operand is 'M' = memory, then assign it to x and/or y.
#         if x == "M":
#             x = memory
#         if y == "M":
#             y = memory
#
#         # Operands must be numbers.
#         # Operator must be one of the following: +, -, *, /
#         try:
#             float(x)
#             float(y)
#         except ValueError:
#             print(msg_1)
#             continue
#         else:
#             if operation not in ["+", "-", "*", "/"]:
#                 print(msg_2)
#                 continue
#             elif operation == "/" and float(y) == 0:
#                 print(msg_3)
#                 continue
#         break
#
#     # Calculates and prints the result of the input equation.
#     result = 0.0
#     match operation:
#         case "+":
#             # noinspection PyRedeclaration
#             result = float(x) + float(y)
#         case "-":
#             # noinspection PyRedeclaration
#             result = float(x) - float(y)
#         case "*":
#             # noinspection PyRedeclaration
#             result = float(x) * float(y)
#         case "/":
#             # noinspection PyRedeclaration
#             result = float(x) / float(y)
#         case _:
#             break
#
#     print(result)
#
#     # Loop for storing the result in memory. It loops until the user chooses 'y = yes' or 'n = no'.
#     while True:
#         print(msg_4)
#         store_input = input()
#
#         if store_input == "y":
#             memory = result
#             break
#         elif store_input == "n":
#             break
#         else:
#             continue
#
#     # Loop for continuing with the calculator. It loops until the user chooses 'y = yes' or 'n = no'.
#     while True:
#         print(msg_5)
#         continue_input = input()
#
#         if continue_input == "n":
#             sys.exit()
#         elif continue_input == "y":
#             break
#         else:
#             continue
#
# # End of Stage 3


# Stage 4
# import sys
#
# # List of input and warning/error messages.
# msg_0 = "Enter an equation"
# msg_1 = "Do you even know what numbers are? Stay focused!"
# msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
# msg_3 = "Yeah... division by zero. Smart move..."
# msg_4 = "Do you want to store the result? (y / n):"
# msg_5 = "Do you want to continue calculations? (y / n):"
# msg_6 = " ... lazy"
# msg_7 = " ... very lazy"
# msg_8 = " ... very, very lazy"
# msg_9 = "You are"
#
#
# # Function definition for checking correct operands and operator.
# def check(v1, v2, v3):
#     msg = ""
#     if is_one_digit(v1) and is_one_digit(v2):
#         msg = msg + msg_6
#     if (v1 == 1 or v2 == 1) and v3 == "*":
#         msg = msg + msg_7
#     if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
#         msg = msg + msg_8
#     if msg != "":
#         msg = msg_9 + msg
#         print(msg)
#
#
# # Function for checking if operand is integer in interval <-10, 10>. Returns True if it is, else False.
# def is_one_digit(v):
#     if v.is_integer() and (-10 < v < 10):
#         output = True
#     else:
#         output = False
#
#     return output
#
#
# # Variable for storing the result of a correct equation.
# memory = 0.0
#
# # Main loop. It loops until the user chooses 'n = no'. Decision-making is done in the inner loop at the end.
# while True:
#     result = 0.0
#     # Loop for checking correct operands and operator.
#     while True:
#         print(msg_0)
#         calc = input().split(" ")
#         # print(calc)
#         x = calc[0]
#         operator = calc[1]
#         y = calc[2]
#
#         # Check if any operand is 'M' = memory, then assign it to x and/or y.
#         if x == "M":
#             x = memory
#         if y == "M":
#             y = memory
#
#         # Operands must be numbers.
#         # Operator must be one of the following: +, -, *, /
#         try:
#             float(x)
#             float(y)
#         except ValueError:
#             print(msg_1)
#             continue
#         if operator not in ["+", "-", "*", "/"]:
#             print(msg_2)
#             continue
#         else:
#             # Functions checks operands and operator.
#             check(float(x), float(y), operator)
#
#             if operator == "/" and float(y) == 0:
#                 print(msg_3)
#                 continue
#
#             # Calculates and prints the result of the input equation.
#             match operator:
#                 case "+":
#                     # noinspection PyRedeclaration
#                     result = float(x) + float(y)
#                 case "-":
#                     # noinspection PyRedeclaration
#                     result = float(x) - float(y)
#                 case "*":
#                     # noinspection PyRedeclaration
#                     result = float(x) * float(y)
#                 case "/":
#                     # noinspection PyRedeclaration
#                     result = float(x) / float(y)
#                 case _:
#                     pass
#
#         break
#
#     print(result)
#
#     # Loop for storing the result in memory. It loops until the user chooses 'y = yes' or 'n = no'.
#     while True:
#         print(msg_4)
#         store_input = input()
#
#         if store_input == "y":
#             memory = result
#             break
#         elif store_input == "n":
#             break
#         else:
#             continue
#
#     # Loop for continuing with the calculator. It loops until the user chooses 'y = yes' or 'n = no'.
#     while True:
#         print(msg_5)
#         continue_input = input()
#
#         if continue_input == "n":
#             sys.exit()
#         elif continue_input == "y":
#             break
#         else:
#             continue
#
# # End of Stage 4


# Stage 5
import sys

# List of input and warning/error messages.
msg_dict = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...",
    4: "Do you want to store the result? (y / n):",
    5: "Do you want to continue calculations? (y / n):",
    6: " ... lazy",
    7: " ... very lazy",
    8: " ... very, very lazy",
    9: "You are",
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
}


# Function for checking simplicity of equation (small integers, 0 or 1; division, multiplication by 1, etc..).
def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_dict[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_dict[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg = msg + msg_dict[8]
    if msg != "":
        msg = msg_dict[9] + msg
        print(msg)


# Function for checking if operand is integer in interval <-10, 10>. Returns True if it is, else False.
def is_one_digit(v):
    if v.is_integer() and (-10 < v < 10):
        output = True
    else:
        output = False

    return output


# Variable for storing the result of a correct equation.
memory = 0.0

# Main loop. It loops until the user chooses 'n = no'. Decision-making is done in the inner loop at the end.
while True:
    result = 0.0
    # Loop for checking correct operands and operator.
    while True:
        print(msg_dict[0])
        calc = input().split(" ")
        # print(calc)
        x = calc[0]
        operator = calc[1]
        y = calc[2]

        # Check if any operand is 'M' = memory, then assign it to x and/or y.
        if x == "M":
            x = memory
        if y == "M":
            y = memory

        # Operands must be numbers.
        # Operator must be one of the following: +, -, *, /
        try:
            float(x)
            float(y)
        except ValueError:
            print(msg_dict[1])
            continue
        if operator not in ["+", "-", "*", "/"]:
            print(msg_dict[2])
            continue
        else:
            # Functions checks operands and operator.
            check(float(x), float(y), operator)

            if operator == "/" and float(y) == 0:
                print(msg_dict[3])
                continue

            # Calculates the result of the input equation.
            match operator:
                case "+":
                    # noinspection PyRedeclaration
                    result = float(x) + float(y)
                case "-":
                    # noinspection PyRedeclaration
                    result = float(x) - float(y)
                case "*":
                    # noinspection PyRedeclaration
                    result = float(x) * float(y)
                case "/":
                    # noinspection PyRedeclaration
                    result = float(x) / float(y)
                case _:
                    pass
        break

    # Prints the result of the input equation.
    print(result)

    # Loop for storing the result in memory. It loops until the user chooses 'y = yes' or 'n = no'.
    while True:
        print(msg_dict[4])
        store_input = input()

        if store_input == "y":
            pass
        elif store_input == "n":
            break
        else:
            continue

        # Loop for storing a simple one-digit result in memory.
        # It loops (max twice e.g., msg_index = 12) until the user chooses 'y = yes' or 'n = no'.
        if is_one_digit(result):
            msg_index = 10
            while msg_index <= 12:
                print(msg_dict[msg_index])
                store_one_digit_input = input()
                if store_one_digit_input == "y" and msg_index == 12:
                    memory = result
                    break
                elif store_one_digit_input == "y":
                    msg_index += 1
                    continue
                elif store_one_digit_input == "n":
                    break
                else:
                    continue
        else:
            memory = result
            break
        break

    # Loop for continuing with the calculator. It loops until the user chooses 'y = yes' or 'n = no'.
    while True:
        print(msg_dict[5])
        continue_input = input()

        if continue_input == "n":
            sys.exit()
        elif continue_input == "y":
            break
        else:
            continue

# End of Stage 5