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

# alternative solution
def moveZerosToEnd(arr: List[int]) -> List[int]:

    nextSpot = 0
    zerocounter = 0
    for idx, element in enumerate(arr):
        if arr[idx] != 0:
            arr[nextSpot] = arr[idx]
            nextSpot += 1
        else:
            zerocounter += 1
    for idx in range(len(arr)-1, len(arr)-1-zerocounter, -1):
        arr[idx] = 0

    return arr
    # runs in O(n)
            
    
# debug your code below
print(moveZerosToEnd([0, 1, 0, 3, 12]))
