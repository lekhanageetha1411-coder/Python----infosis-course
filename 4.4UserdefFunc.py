def fact_user(n):
    print("the factors of",n,"is:")
    for i in range(1,n+1):
        if(n % i) == 0:
            print(i)

nm = int(input("Enter the number to see a factors:"))            

fact_user(nm)
