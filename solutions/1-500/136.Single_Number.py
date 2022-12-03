from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        nums = sorted(nums)
        i = 0

        while i < len(nums) - 1:

            if nums[i] != nums[i + 1]:
                return nums[i]

            i += 2

        return nums[-1]
