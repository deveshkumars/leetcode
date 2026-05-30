def get_different_number(arr):
  hashmap = {}
  MAX_INT = 2**31 - 1
  for x in arr:
    hashmap[str(x)] = True
  for i in range(0, MAX_INT):
    if str(i) in hashmap:
      continue
    else:
      return i
  
# debug your code below
arr = [0, 2, 1, 3, 5]
print(get_different_number(arr))
