from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        visited = {}

        for i in range(len(nums)):

            if nums[i] in visited:
                continue

            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
