from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        count_even = 0

        for i in range(0, len(nums)):
            num_str = str(nums[i])

            if len(num_str) % 2 == 0:
                count_even += 1

        return count_even
