n = int(input("ENter n1:"))

n1, n2 = 0, 1
Count = 0

if n <= 0:
    print("please enter a positive number")
elif n == 1:
    print(n,"fibonacci uptill :")    
    print(n1)
else:
    print("Fibonacci sequence is :")    
    while Count < n:
        print(n1)
        vartemp =n1 + n2
        n1 = n2
        n2 = vartemp
        Count += 1
