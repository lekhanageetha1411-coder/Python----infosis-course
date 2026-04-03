num1 = int(input("Enter a number to check if it is prime no "))

if num1 > 1:
    for i in range(2,num1):
        if(num1 % i)==0:
            print(num1,"is not a prime")
            print(i,"times",num1//i,"is",num1)
            break

    else:
        print(num1, "is a prime")

else:
    print(num1,"is not a prime")        



min = int(input("Enter the min range:"))
max = int(input("Enter the max range:"))

for i in range(min,max+1):
    if i > 0:
        for j in range(2,i):
            if(i % j)==0:
                break

        else:
            print(i)



num1 = int(input("Enter the number to check a prime or not::"))

varf = False

if num1 > 1:
    for i in range(2,num1):
        if(num1 % i == 0):
            varf = True
        break

if varf:
    print(num1," is not a prime")

else:
    print(num1," is a prime")
