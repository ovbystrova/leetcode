from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        if letters[-1] <= target:
            return letters[0]

        left, right = 0, len(letters) - 1

        while left < right:

            mid_id = (left + right) // 2
            mid_value = letters[mid_id]

            if mid_value == target and letters[mid_id + 1] != target:
                return letters[mid_id + 1]

            elif mid_value > target:
                right = mid_id

            else:  # mid_value < target
                left = mid_id + 1

        return letters[right + 1] if letters[right] == target else letters[right]
