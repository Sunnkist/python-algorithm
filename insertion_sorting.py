arr = [7,4,6,3,5,0,1,2,9,8]

for i in range(1,len(arr)):#from position 1(second data in the array)
    for j in range(i,0,-1):     
        if arr[j-1] > arr[j]: #if L>R
            arr[j], arr[j-1] = arr[j-1], arr[j] #swap
        else: #L<R
            break

print(arr) 
