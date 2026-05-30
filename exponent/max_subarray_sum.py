from typing import List

# [-2, 1, -3, 4, -1, 2, 1, -5, 4] = 1
# [-2, -1, -4, 0, -1, 1, 2, -3, 1] prefix
# [1, 3, 2, 5, 1, 2, 0, -1, 4] suffix

def max_subarray_sum(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    
    local_max = global_max = nums[0]

    for i in range(1, len(nums)):
        local_max = max(nums[i], local_max + nums[i])
        global_max = max(local_max, global_max)

    return global_max

# second scuffed soln
# def max_subarray_sum(nums: List[int]) -> int:
#     total_sum = calc_total_sum(nums)
#     prefix = calc_prefix(nums)
#     suffix = calc_suffix(nums)
#     left = 0
#     right = len(nums) - 1
#     curr_sum = 

# def calc_total_sum(nums: List[int]) -> int:
#     sum = 0
#     for x in nums:
#         sum += x
#     return sum

# def calc_prefix(nums):
#     new = [0 for x in nums]
#     new[0] = nums[0]
#     for i in range(len(nums)):
#         if i != 0:
#             new[i] = new[i - 1] + nums[i]
#     return new

# def calc_suffix(nums):
#     new = [0 for x in nums]
#     new[-1] = nums[-1]
#     for i in range(len(nums) - 1, -1, -1):
#         if i != len(nums) - 1:
#             new[i] = new[i + 1] + nums[i]
#     return new

# scuffed
# def max_subarray_sum(nums: List[int]) -> int:
#     if len(nums) == 0:
#         return 0
#     curr_max = nums[0]
#     curr_sum = nums[0]
#     left = 0
#     right = 0
#     while right < len(nums) - 1:
#         right += 1
#         curr_sum = curr_sum + nums[right]
#         curr_max = max(curr_sum, curr_max)
#         if nums[left] < 0:
#             curr_sum = curr_sum - nums[left]
#             left += 1
#             curr_max = max(curr_sum, curr_max)

#     return curr_max

# debug your code below
print(max_subarray_sum([-1, 2, -3, 4]))
print(max_subarray_sum([2, 3, -2, 4]))
print(max_subarray_sum([1, -1, -5, -4]))
print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
