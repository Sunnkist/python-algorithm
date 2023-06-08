array=[5,3,6,5,72,4,65,32]

#make a new array
#arr len is max value of array + 1 or 2 buffer
count=[0]*(max(array)+1) 

for i in range(len(array)):
    count[array[i]]+=1

for i in range(len(count)):
    for j in range(count[i]): # multiple val ex)2 
        print(i, end=' ')      #print multiple times

