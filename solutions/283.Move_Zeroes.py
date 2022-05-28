from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        zeros_before_element = 0

        for i in range(0, len(nums)):
            if nums[i] == 0:
                zeros_before_element += 1
                continue

            nums[i - zeros_before_element], nums[i] = nums[i], nums[i - zeros_before_element]
#             tmp = nums[i-zeros_before_element]
#             nums[i-zeros_before_element] = nums[i]
#             nums[i] = tmp
