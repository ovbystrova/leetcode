from typing import List


# Time Complexity O(logN), Space Complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums) - 1

        while left < right:

            mid_id = (left + right) // 2
            mid_value = nums[mid_id]

            if mid_value > nums[right]:
                left = mid_id + 1
            else:
                right = mid_id if nums[right] != mid_value else right - 1

        return nums[left]