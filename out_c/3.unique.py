arr = [1,2,2,4,6,7,5,4,6,6,6,9]

for i in range(len(arr)):
    c = 0
    for j in range(len(arr)):
        if(arr[i] == arr[j])and(i != j):
            c = c+1
    if c == 0:
        print(arr[i])
