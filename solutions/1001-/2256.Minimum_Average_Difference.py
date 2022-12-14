from typing import List

class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        min_id = 0
        min_avg = 10**5
        prefix_summ = 0
        total_summ = sum(nums)
        n = len(nums)

        for i in range(len(nums)):
            prefix_summ += nums[i]
            before = prefix_summ // (i+1)
            if i == n - 1:
                after = 0
            else:
                after = (total_summ - prefix_summ) // (n - i - 1)
            average = abs(before - after)

            if average == 0:
                return i
            elif average < min_avg:
                min_id = i
                min_avg = average

        return min_id
