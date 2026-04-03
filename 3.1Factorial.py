num1 = int(input("Enter the num1 :"))
varFact = 1

if num1 < 0:
    print("ohh sorry , factorial is not available for -ve numbers")
elif num1 == 0:
    print("Factorial of the 0 is 1")    
else:
    for i in range(1,num1+1):
        varFact = varFact * i
    print(num1,"factorial is ",varFact)
