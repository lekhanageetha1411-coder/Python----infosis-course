num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

print("The number 1 before swap :{}".format(num1))
print("The number 2 before swap :{}".format(num2))

temp = num1
num1 = num2 
num2 = temp

print("The number 1 before swap :{}".format(num1))
print("The number 2 before swap :{}".format(num2))




or


num1 = int(input("Enter the number one value:"))
num2 = int(input("Enter the number 2 value:"))

print("the value of num1 before swapping = ",num1)
print("the value of num2 before swapping = ",num2)

num1,num2 = num2,num1

print("the value of num1 after swapping = ",num1)
print("the value of num2 after swapping = ",num2)
