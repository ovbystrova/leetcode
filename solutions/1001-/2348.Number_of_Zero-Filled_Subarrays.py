from typing import List


class Solution:

    def zeroFilledSubarray(self, nums: List[int]) -> int:

        total_subarrays = 0
        current_subarrays = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                current_subarrays += 1
                total_subarrays += current_subarrays
                continue
                
            current_subarrays = 0
        return total_subarrays
