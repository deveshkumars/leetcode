def climb_stairs(n: int) -> int:
    stair_cache = []
    for i in range(n+1):
        if i == 0:
            stair_cache.append(0)
        elif i == 1:
            stair_cache.append(1)
        elif i == 2:
            stair_cache.append(2)
        else:
            stair_cache.append(stair_cache[i-1]+stair_cache[i-2])
    return stair_cache[n]
    

# debug your code below
print(climb_stairs(3))