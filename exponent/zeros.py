from typing import List

def moveZerosToEnd(arr: List[int]) -> List[int]:
    left = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            pass
        else:
            if left != right:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            left += 1
    return arr
            
    
# debug your code below
print(moveZerosToEnd([0, 1, 0, 3, 12]))
