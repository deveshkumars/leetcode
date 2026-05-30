from typing import List

# two pointer soln

def productExceptSelf(nums: List[int]) -> List[int]:
    prefix = calc_prefix(nums)
    suffix = calc_suffix(nums)
    for i in range(len(nums)):
        if i == 0:
            nums[i] = suffix[1]
        elif i == (len(nums) - 1):
            nums[i] = prefix[i - 1]
        else:
            nums[i] = prefix[i - 1] * suffix[i + 1]
        # print(nums)
    return nums

def calc_prefix(nums: List[int]) -> List[int]:
    nums1 = [1 for x in nums]
    nums1[0] = nums[0]
    for i in range(len(nums1)):
        if i != 0:
            nums1[i] = nums[i] * nums1[i - 1]
    return nums1

print(calc_prefix([1, 2, 3, 4]))

def calc_suffix(nums: List[int]) -> List[int]:
    nums1 = [1 for x in nums]
    nums1[-1] = nums[-1]
    for i in range(len(nums1) - 1, -1, -1):
        if i != len(nums1) - 1:
            nums1[i] = nums[i] * nums1[i + 1]
    return nums1

print(calc_suffix([1, 2, 3, 4]))


# linear soln w/division
# def productExceptSelf(nums: List[int]) -> List[int]:
#     prefix_nums = calc_prod(nums)
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums[i] = int(prefix_nums)
#         else:
#             nums[i] = int(prefix_nums / nums[i])
#     return nums

# def calc_prod(nums: List[int]) -> int:
#     prod = 1
#     for i in range(len(nums)):
#         prod *= nums[i]
#     return prod

# O(n^2) soln
# def productExceptSelf(nums: List[int]) -> List[int]:
#     new = []
#     for i in range(len(nums)):
#         new.append(find_prod_wo(nums, i))
#     return new

# def find_prod_wo(nums: List[int], i: int) -> int:
#     prod = 1
#     for j in range(len(nums)):
#         if i != j:
#             prod = prod * nums[j]
#     return prod

# debug your code below
print(productExceptSelf([1, 2, 3, 4]))
