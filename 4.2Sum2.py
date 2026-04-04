num = int(input("Enter the num1 :"))

sum = 0

if num < 0:
    print("Please enter the positive number:")
else:
    while(num > 0):
        sum += num
        print("num is:",num,"the sum is :",sum)
        num -= 1
    
