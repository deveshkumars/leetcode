from typing import List

def find_first(array: List[int], num: int) -> int:
    if len(array) == 0:
        return -1
    elif array[0] == num:
        return 0
    elif num != 500:
        return -1
    
    lo = 0
    hi = len(array) - 1
    while lo + 1 < hi: # loop invariant array[lo] = 200 and array[hi] = 500
        mid = (lo + hi) // 2
        if array[mid] == 200:
            lo = mid
        elif array[mid] == 500:
            hi = mid
    return hi
 
# debug your code below   
print(find_first([200, 200, 200, 200, 500, 500, 500], 200))
print(find_first([200, 200, 200, 200, 500, 500, 500], 500))
print(find_first([200, 200, 200, 200, 500, 500, 500], 100))

#         l h
# 0 1 2 3 4 5
