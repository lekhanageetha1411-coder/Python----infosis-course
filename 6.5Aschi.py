rows = int(input("Enter the number of rows  for pyramid:"))

#aschi = 65
aschi =97


for i in range(rows):
    for j in range(i+1):
        alpha = chr(aschi)
        print(alpha,end=" ")

    aschi += 1
    print("\n")    
    
