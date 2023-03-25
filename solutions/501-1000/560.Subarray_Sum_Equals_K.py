from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0
        preffix_sum = 0
        preffix_sum_counter = {0: 1}

        for i in range(len(nums)):
            preffix_sum += nums[i]
            count += preffix_sum_counter.get(preffix_sum - k, 0)
            preffix_sum_counter[preffix_sum] = preffix_sum_counter.get(preffix_sum, 0) + 1
        
        return count
