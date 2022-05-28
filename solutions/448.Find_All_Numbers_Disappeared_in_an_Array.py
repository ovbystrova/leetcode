from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        nums.sort()

        missed_elements = []

        i, j = 1, 0

        while j < len(nums) and i <= len(nums):

            if i > nums[j]:
                j += 1

            elif i < nums[j]:
                missed_elements.append(i)
                i += 1

            else:  # i = nums[j]
                i += 1
                j += 1

        missed_elements.extend([_ + 1 for _ in range(nums[j - 1], len(nums))])
        return missed_elements
