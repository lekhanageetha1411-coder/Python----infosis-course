arr = [1,2,3,4,9,5,6,7]
max_prod = 0

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]*arr[j]>max_prod):
            max_prod = arr[i] * arr[j]
print(max_prod)            
