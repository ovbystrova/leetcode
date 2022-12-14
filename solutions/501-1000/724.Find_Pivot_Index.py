from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sums_left = 0
        prefix_sums_right = sum(nums) - prefix_sums_left - nums[0]

        if prefix_sums_left == prefix_sums_right:
            return 0

        for i in range(1, len(nums)):

            prefix_sums_left += nums[i-1]
            prefix_sums_right -= nums[i]

            if prefix_sums_left == prefix_sums_right:
                return i

        return -1