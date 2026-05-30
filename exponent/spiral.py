from typing import List

def spiral_copy(inputMatrix: List[List[int]]) -> List[int]:
    forward = True
    x = True
    visited = {}
    visited_len = 0
    new = []
    loc = (0, 0)
    old_loc = (0, 0)
    max_width = len(inputMatrix[0])
    max_height = len(inputMatrix)
    counter = 0
    while visited_len < max_height * max_width:
        
        if loc[0] >= max_width:
            # bring it back to normal x
            old_loc = loc
            loc = (loc[0] - 1, loc[1])
            # make it go down
            x = False # so y
            forward = True # so down
        elif loc[0] < 0:
            old_loc = loc
            loc = (0, loc[1])
            # make it go up
            x = False # so y
            forward = False # so up
        elif loc[1] >= max_height:
            # bring it back
            old_loc = loc
            loc = (loc[0], loc[1] - 1)
            # make it go left
            x = True
            forward = False
        elif loc[1] < 0:
            print("Error")
            # should not be possible
        elif str(loc) not in visited:
            # add to visited
            visited[str(loc)] = True
            visited_len += 1
            new.append(inputMatrix[loc[1]][loc[0]])
            print(loc)
            # increment visited_len
            # if forward and x:
            #     loc = (loc[0] + 1, loc[1])
            # elif not forward and x:
            #     loc = (loc[0] - 1, loc[1])
            # elif forward and not x:
            #     loc = (loc[0], loc[1] + 1)
            # elif not x and not forward:
            #     loc = (loc[0], loc[1] - 1)
        else:
            loc = old_loc
            if forward and x:
                x = False
            elif not forward and x:
                x = False
            elif forward and not x:
                x = True
                forward = False
            else:
                forward = True
                x = True
        old_loc = loc
        if forward and x:
            loc = (loc[0] + 1, loc[1])
        elif not forward and x:
            loc = (loc[0] - 1, loc[1])
        elif forward and not x:
            loc = (loc[0], loc[1] + 1)
        elif not x and not forward:
            loc = (loc[0], loc[1] - 1)
    return new

# debug your code below
inputMatrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(spiral_copy(inputMatrix))
