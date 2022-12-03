from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        i = 0
        for element in nums:
            if element != val:  # If element == val then we owerride val with element value in the next step
                nums[i] = element
                i += 1

        return i
