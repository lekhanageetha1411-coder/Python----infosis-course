def funcAdd(x,y):
    return x+y
def funcSub(x,y):
    return x-y
def funcmul(x,y):
    return x*y
def funcDiv(x,y):
    return x/y

print("select your choice:")
print("\n 1. Add")
print("\n 2.Sub")
print("\n 3.Mul")
print("\n4.div")

while True:
    ch = input("Enter your any one choice(1\2\3\4):")
    num1 = float(input("Enter the num1:"))
    num2 = float(input("ENter the num2:"))
    if ch in('1','2','3','4'):
        if ch == '1':
            print(num1,"+",num2,"=",funcAdd(num1,num2))

        elif ch == '2':
            print(num1,"-",num2,"=",funcSub(num1,num2))     

        elif ch == '3':
            print(num1,"*",num2,"=",funcmul(num1,num2))  

        elif ch == '4':
            print(num1,"+",num2,"=",funcDiv(num1,num2)) 
            break
    else:
            print("invalid choice!")
