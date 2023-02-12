from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        prev = current = max_ones = 0

        for item in nums:
            if item == 1:
                current += 1
                max_ones = max(current + prev, max_ones)
                continue

            # Consider That the first zero can be switched to 1
            prev, current = current + 1, 0
            max_ones = max(prev, max_ones)

        return max_ones
