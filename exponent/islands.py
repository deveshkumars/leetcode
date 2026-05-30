from typing import List

visited = {}
parents = {}


# finds
def fynd(island_loc: str) -> str:
    """Finds"""
    if (island_loc == parents[island_loc]):
        return island_loc
    else:
        return fynd(parents[island_loc])
# parents[str((1,2))] = str((1,3))
# parents[str((1,3))] = str((1,4))
# parents[str((1,4))] = str((1,4))
# print(fynd(str((1,2)))) 

def union(island_loc_1: str, island_loc_2: str):
    """union"""
    if island_loc_1 in parents:
        p1 = fynd(island_loc_1)
    else:
        parents[str(island_loc_1)] = str(island_loc_1)
        p1 = str(island_loc_1)
    if island_loc_2 in parents:
        p2 = fynd(island_loc_2)
    else:
        parents[str(island_loc_2)] = str(island_loc_2)
        p2 = str(island_loc_2)

    if (p1 == p2):
        return
    else:
        if (p1 < p2):
            parents[str(island_loc_2)] = p1
        else:
            parents[str(island_loc_1)] = p2
    visited[str(island_loc_1)] = True
    visited[str(island_loc_2)] = True
    # print(parents)

def get_number_of_islands(binaryMatrix: List[List[int]]) -> int:
    

    n = len(binaryMatrix)
    if (n == 0):
        return -1
    m = len(binaryMatrix[0])
    if (m == 0):
        return -1

    def helper(i:int, j:int):
        if i != 0 and binaryMatrix[i-1][j] == 1:
            union(str((i,j)), str((i-1,j)))
        if i != (n-1) and binaryMatrix[i+1][j] == 1:
            union(str((i,j)), str((i+1, j)))
        if j != 0 and binaryMatrix[i][j-1] == 1:
            union(str((i,j)), str((i, j - 1)))
        if j != (m-1) and binaryMatrix[i][j+1] == 1:
            union(str((i,j)), str((i, j + 1)))
        if str((i,j)) not in parents:
            union(str((i,j)), str((i,j)))

    for i in range(n):
        for j in range(m):
            if binaryMatrix[i][j] == 1 and binaryMatrix[i][j] not in visited:
                    helper(i,j)
    # print(parents)
    count = {}
    for x in parents:
        if parents[x] in count:
            pass
        else:
            count[parents[x]] = True

    # print(parents)
    parents.clear()
    visited.clear()
    return len(count)
    
# debug your code below
binaryMatrix = [
    [0, 1, 0, 1, 0],
    [0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1]
]

print(get_number_of_islands(binaryMatrix))
print(get_number_of_islands([[0]]))
