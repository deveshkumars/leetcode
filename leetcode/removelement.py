class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        opening = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                k += 1
                if i != opening:
                    nums[opening] = nums[i]
                opening += 1
        return k

