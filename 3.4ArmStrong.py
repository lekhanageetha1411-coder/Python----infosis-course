num1  = int(input("Enter the num1"))

sum = 0
temp = num1

while temp > 0:
    d = temp % 10
    sum += d ** 3
    temp //= 10

if num1 == sum:
    print(num1,"is a armstrong")    
else:
    print(num1,"is not an armstrong")    
