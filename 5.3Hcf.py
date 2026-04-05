def calc_hcf(x, y):

    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i

    return hcf


def calc_lcm(x, y):

    lcm = (x * y) // calc_hcf(x, y)
    return lcm


# User input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Output
print("HCF is:", calc_hcf(num1, num2))
print("LCM is:", calc_lcm(num1, num2))
