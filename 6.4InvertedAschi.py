rows = int(input("Enter the num of rows:"))

aschi = 97

for i in range(rows,0,-1):
    for j in range(1,i+1):
        alpha = chr(aschi)
        print(alpha,end=" ")
    aschi += 1
    print("\n")
