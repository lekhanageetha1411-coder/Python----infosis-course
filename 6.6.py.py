rows = int(input("Enter no of rows:"))

for i in range(rows):
    #spaceRow 0 → 0 spaces,Row 1 → 1 space,Row 2 → 2 spaces,Row 3 → 3 spaces,Row 4 → 4 spaces
    for space in range(i):
        print(" ",end="")

        #*
    for j in range(rows-i):
        print("*",end=" ")
    print()        
