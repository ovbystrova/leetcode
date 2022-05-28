from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        result = []

        left, right = 0, len(nums) - 1

        while left < right:
            left_value = nums[left]
            right_value = nums[right]

            if abs(left_value) > abs(right_value):
                result.insert(0, left_value * left_value)
                left += 1

            else:
                result.insert(0, right_value * right_value)
                right -= 1

        right_value = nums[right]
        result.insert(0, right_value * right_value)

        return result
