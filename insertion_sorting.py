arr = [7,4,6,3,5,0,1,2,9,8] 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i             #initialize index as min value
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: #if value behind is bigger
                min_idx = j     #set min index as the value behind
        arr[i], arr[min_idx] = arr[min_idx], arr[i] 
        #swap values between index start position and min value(behind) 
        # 인덱스 시작한 위치와 제일 작은 값 서로 자리 바꿈

    return arr

print(selection_sort(arr))