# Devesh's Leetcode Guide

## Links
[link to dsa](https://www.w3schools.com/dsa/index.php)

## Python Mechanics

### Files and input management
```python
import sys

sys.stdin = open("paint.in", "r")
sys.stdout = open("paint.out", "w")

arr1 = [int(x) for x in input().split(" ").strip("\n")]
list(x) = x as a list


Better input method
arr = [int(x) for x in input().split()]
arr2 = [int(x) for x in input().split()]
print(arr)

input()
.split(" ")
int(x)
```

### Important Math Operations
```python
5 // 2 # rounds down
5 ** 2 # 5 to the second power
```

### List Operations
```python
example_list = []
example_list.append() # appends something to the list
example_list.pop(x) # pops off something at index x, defaults to last element
x = [0] * 50 # returns [0, 0 ,0 ,0 ,0 ,0 ,0 ,0, ]
x = [[0] for x in range(5)] # returns [[0], [0]]
```

### Iterators
```python
arr = [1, 2, 3]
it = iter(arr)
print(next(it)) #1
print(next(it)) #2
# error occurs when you reach an element that has not been initialized
```

### List Comprehensions
```python
old_list = [2, 7, 4, 6, 75]
new_list = [i for i in old_list if i % 2 == 1]
new_list = [7, 75]
```

### Primitives
```python
{5, 5,5 0} # set
{'hi' : 5} # hashmaps/dict

array = [0, 1, 2, 2, 2] # arraylist

if array[2] not in array:
    print(False)
```

### Sorting
```python
l.sort(reverse=True)
l = sorted(l, reverse=False, key=??)

def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
```

### Letters
```python
import string
string.ascii_lowercase
```

## Problem Types
[Exponent Course](https://www.tryexponent.com/courses/software-engineering/swe-practice/swe-tips)

### Arrays



### Hash Tables



