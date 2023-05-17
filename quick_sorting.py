
array=[5,3,6,5,72,4,65,32]

def quick_sort(array):
    #if list has 1 element or less(empty) then return
    if len(array)<=1:
        return array

    pivot = array[0]
    tail = array[1:]
    #put elements on left side, if smaller than the pivot
    #put elements on left side, if bigger than the pivot
    left_side = [x for x in tail if x<=pivot]
    right_side = [x for x in tail if x>pivot]

    return quick_sort(left_side)+[pivot]+quick_sort(right_side)

print(quick_sort(array))