class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        hashmap = {}
        smalls = 0
        for i in range(len(nums)):
            if i == 0:
                hashmap[sorted_nums[i]] = 0
            elif sorted_nums[i] == sorted_nums[i-1]:
                hashmap[sorted_nums[i]] = hashmap[sorted_nums[i-1]]
            else:
                hashmap[sorted_nums[i]] = i
        for i in range(len(nums)):
            nums[i] = hashmap[nums[i]]
        return nums
