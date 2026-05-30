from typing import List

def find_duplicates(arr1: List[int], arr2: List[int]) -> List[int]:
    # easy soln return sorted(list(set(arr1) & set(arr2)), reverse=False)
    
    # second soln
    # hash_map = {}
    # new = []
    # for x in arr1:
    #     hash_map[str(x)] = True
    # for x in arr2:
    #     if str(x) in hash_map:
    #         new.append(x)
    # return new

    new = []
    for x in arr1:
        if binary_search(arr2, x):
            new.append(x)
    return new

def binary_search(arr, x):
    if len(arr) == 1:
        if arr[0] == x:
            return True
        else:
            return False
    else:
        mid = (len(arr) - 1) // 2
        print(mid)
        if arr[mid] == x:
            return True
        elif arr[mid] > x:
            return binary_search(arr[0:mid+1], x)
        elif arr[mid] < x:
            return binary_search(arr[mid+1:], x)

print(binary_search([1, 2],23))
    
        
  
# debug your code below
print(find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]))
