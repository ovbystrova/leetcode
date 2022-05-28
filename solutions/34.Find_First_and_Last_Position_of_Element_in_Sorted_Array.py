from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1, -1]

        left, right = 0, len(nums) - 1

        while (left + 1) < right and nums[left] != nums[right]:

            mid_id = (left + right) // 2
            mid_value = nums[mid_id]

            if mid_value > target:
                right = mid_id

            elif mid_value < target:
                left = mid_id

            else:  # mid_value == target

                left_to_mid = mid_id - 1
                right_to_mid = mid_id + 1

                while left_to_mid > left and nums[left_to_mid] == target:
                    left_to_mid -= 1
                left = left_to_mid + 1 if nums[left_to_mid] != target else left_to_mid

                while right_to_mid < len(nums) - 1 and nums[right_to_mid] == target:
                    right_to_mid += 1
                right = right_to_mid - 1 if nums[right_to_mid] != target else right_to_mid

        if nums[left] == nums[right] == target:
            return [left, right]
        elif nums[left] == target:
            return [left, left]
        elif nums[right] == target:
            return [right, right]
        else:
            return [-1, -1]
