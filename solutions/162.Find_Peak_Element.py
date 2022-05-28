from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        length = len(nums)

        if length == 1:
            return 0

        elif length == 2:
            return 0 if nums[0] > nums[1] else 1

        left, right = 0, length - 1

        while left < right:

            mid_id = (left + right) // 2
            mid_value = nums[mid_id]

            next_item = nums[mid_id + 1] if mid_id + 1 < length else nums[-1]
            prev_item = nums[mid_id - 1] if mid_id - 1 > 0 else nums[0]

            if (mid_value > next_item) and (prev_item < mid_value):
                return mid_id

            else:
                if prev_item < mid_value:
                    left = mid_id + 1
                else:
                    right = mid_id

        return left
