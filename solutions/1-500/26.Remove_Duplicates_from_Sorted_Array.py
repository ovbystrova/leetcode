from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        current_element = None
        for element in nums:
            if element == current_element:
                continue
            nums[i] = element
            current_element = element
            i += 1

        return i
