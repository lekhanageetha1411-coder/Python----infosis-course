rows = int(input("Enter the num of rows for pyramid:"))

for i in range(0,rows):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
