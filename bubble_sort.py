array_=[5,3,6,2,72,4,65,32]

def bubble(array):
    for i in range(len(array)):
        for j in range(1, len(array)-i):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                pass
    return array

print(bubble(array_))