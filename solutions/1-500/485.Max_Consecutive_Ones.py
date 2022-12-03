from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        inside_ones = False
        max_ones = 0
        current_ones = 0

        for i in range(0, len(nums)):
            if nums[i] == 1:
                inside_ones = True
                current_ones += 1

            elif nums[i] == 0:
                inside_ones = False

                if current_ones > max_ones:
                    max_ones = current_ones

                current_ones = 0

        if current_ones > max_ones:
            max_ones = current_ones

        return max_ones
