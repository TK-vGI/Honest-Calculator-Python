# Stage 1
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

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
    break