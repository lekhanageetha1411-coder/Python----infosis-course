arr = [1,2,3,4,5]
even = []
odd = []
for i in range(len(arr)):
    if arr[i]%2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
print("the even num:",even)        
print("the odd num:",odd)