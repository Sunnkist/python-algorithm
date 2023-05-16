arr = [7,4,6,3,5,0,1,2,9,8]

for i in range(len(arr)):
    min = i;            #initialize min as i (i:from 0 to last)
    for j in range(i+1, len(arr)):
        if arr[min] > arr[j]:
            min = j     #mark minimun value in the rest of the array
    print(arr)
    arr[i], arr[min] = arr[min], arr[i] #swap min value with the arr[i]
    #as i goes bigger, array sorted in smallest, 2nd smallest, .., last.

print(arr)