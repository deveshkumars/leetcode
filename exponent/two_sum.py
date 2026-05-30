from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    hitlist = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if str(complement) in hitlist:
            return [hitlist[str(complement)], i]
        else:
            hitlist[str(nums[i])] = i
    return []
    
    # brute force runtime O(n^2): 77ms
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j and nums[i] + nums[j] == target:
    #             return [i, j]
    # return []
    
# debug your code below
print(two_sum([2, 7, 11, 15], 9))
