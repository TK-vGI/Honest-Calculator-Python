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


# Stage 2
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."

while True:
    print(msg_0)
    calc = input().split(" ")
    # print(calc)
    x = calc[0]
    operation = calc[1]
    y = calc[2]

    try:
        float(x)
        float(y)
    except ValueError:
        print(msg_1)
        continue
    else:
        if operation not in ["+", "-", "*", "/"]:
            print(msg_2)
            continue
        elif operation == "/" and float(y) == 0:
            print(msg_3)
            continue
    break

result = 0.0

if operation == "+":
    result = float(x) + float(y)
elif operation == "-":
    result = float(x) - float(y)
elif operation == "*":
    result = float(x) * float(y)
elif operation == "/":
    result = float(x) / float(y)

print(result)

# End of Stage 2