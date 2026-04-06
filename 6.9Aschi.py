n = 4

aschi = 97

for i in range(0,n):

    for j in range(n-i-1):
        print(" ",end="")
    for k in range(i+1):
        alpa = chr(aschi)
        print(alpa,end=" ")
        aschi += 1
    print()
