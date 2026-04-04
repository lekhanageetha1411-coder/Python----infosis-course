def funcAdd(x,y,z):
    return x+y+z
def funcSub(x,y,z):
    return x-y-z
def funcmul(x,y,z):
    return x*y*z
def funcDiv(x,y):
    return x/y

print("select your choice:")
print("\n 1. Add")
print("\n 2.Sub")
print("\n 3.Mul")
print("\n4.div")

while True:
    ch = input("Enter your any one choice(1\2\3\):")

    if ch in('1','2','3'):
        num1 = float(input("Enter the num1:"))
        num2 = float(input("ENter the num2:"))
        num3 = float(input("ENter the num3:"))

        if ch == '1':
            print(num1,"+",num2,"+",num3,"=",funcAdd(num1,num2,num3))

        elif ch == '2':
            print(num1,"-",num2,"-",num3,"=",funcSub(num1,num2,num3))     

        elif ch == '3':
            print(num1,"*",num2,"*",num3,"4=",funcmul(num1,num2,num3))  
            break
    elif ch == '4':
        num1 = float(input("Enter the num1:"))
        num2 = float(input("ENter the num2:"))


    
        print(num1,"/",num2,"=",funcDiv(num1,num2)) 
        break
    else:
        print("invalid choice!")
