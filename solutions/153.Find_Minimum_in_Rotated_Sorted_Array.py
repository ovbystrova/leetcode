from typing import List


# Time Complexity O(logN), Space Complexity O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:

        left, right = 0, len(nums)
        min_el = nums[-1]

        while left < right:

            mid_id = (left + right) // 2
            mid_value = nums[mid_id]

            if mid_value < min_el:
                min_el = mid_value

            do_reverse = True if (mid_value > nums[-1]) else False

            if do_reverse:
                left = mid_id + 1
            else:
                right = mid_id

        return min_el
