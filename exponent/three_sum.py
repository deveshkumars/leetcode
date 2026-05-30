from typing import List

# O(n^2) solution

# Brute force
# def three_sum(nums: List[int]) -> List[List[int]]:
#     solns = []
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#             for k in range(len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0 and i != j and i != k and j != k:
#                     solns.append((nums[i], nums[j], nums[k]))
#     return unique(solns)

def three_sum(nums: List[int]) -> List[List[int]]:
    solns = []
    for i in range(len(nums)):
        woi = [nums[j] for j in range(len(nums)) if i != j]
        ts = two_sum(woi, -1 * nums[i])
        solns = solns + (list(map(lambda x: x + [nums[i]], ts)))

    return unique(solns)

def two_sum(woi, target):
    hitlist = {}
    output = []
    for i in range(len(woi)):
        complement = target - woi[i]
        if str(complement) in hitlist:
            output.append([woi[i], complement])
        else:
            hitlist[str(woi[i])] = i
    return output

def unique(solns: List):
    new = []
    for x in solns:
        flag = True
        for y in new:
            if x == y:
                flag = False
            elif set([x[0], x[1], x[2]]) == set([y[0], y[1], y[2]]) and x[0] + x[1] + x[2] == y[0] + y[1] + y[2]:
                flag = False
        if flag:
            new.append([x[0], x[1], x[2]])
    return new



print(three_sum([0, 1, -1]))
