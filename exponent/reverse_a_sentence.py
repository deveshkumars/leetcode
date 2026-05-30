from typing import List

# O(n) soln with constant space
def reverse_words(arr: List[str]) -> List[str]:
    arr.reverse()

    start = 0
    for i in range(len(arr)):
        if arr[i][0] == " ":
            arr[start:i] = list(reversed(arr[start:i]))
            start = -1
        elif start == -1:
            start = i
        else:
            pass
    arr[start:] = list(reversed(arr[start:]))
    return arr



  
# debug your code below
arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
        'm', 'a', 'k', 'e', 's', '  ',
        'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

print(reverse_words(arr))
