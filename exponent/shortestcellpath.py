from typing import List


def shortestCellPath(grid: List[List[int]], sr: int, sc: int, tr: int, tc: int) -> int:
    m = len(grid)
    n = len(grid[0])
    visited = {}
    def findNeighbors(i, j, dist) -> List[tuple]:
        neighbors = []
        if i != 0 and grid[i-1][j] == 1 and str((i-1,j)) not in visited:
            neighbors.append((i-1,j,dist+1))
        if i != (m-1) and grid[i+1][j] == 1 and str((i+1,j)) not in visited:
            neighbors.append((i+1,j,dist+1))
        if j != 0 and grid[i][j-1] == 1 and str((i,j-1)) not in visited:
            neighbors.append((i,j-1,dist+1))
        if j != (n-1) and grid[i][j+1] == 1 and str((i,j+1)) not in visited:
            neighbors.append((i,j+1,dist+1))
        return neighbors
    


    def BFS():
        queue = []
        queue.append((sr,sc,0))
        while (len(queue) > 0):
            # print(visited, queue)
            deq = queue.pop()
            visited[str((deq[0],deq[1]))] = True
            if deq[0] == tr and deq[1] == tc:
                return deq[2]
            queue += findNeighbors(deq[0], deq[1], deq[2])
        return -1

    return BFS()
    

    
    
	
# debug your code below
grid = [[1, 1, 1, 1], [0, 0, 0, 1], [1, 1, 1, 1]]
sr, sc, tr, tc = 0, 0, 2, 0
print(shortestCellPath(grid, sr, sc, tr, tc))
