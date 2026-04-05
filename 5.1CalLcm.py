def cal_lcm(x, y):

    if x > y:
        g = x
    else:
        g = y

    while True:
        if (g % x == 0) and (g % y == 0):
            lcm = g
            break
        g += 1

    return lcm


x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

print("The LCM is:", cal_lcm(x, y))
