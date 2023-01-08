from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        longest = prev = current = 0
        for item in nums:
            if item == 1:
                current += 1
                longest = max(longest, prev + current)
            else:
                # at first time set prev to current because maybe the next is 1
                # at second stem prev would be zero
                prev, current = current, 0

        return longest - (longest == len(nums))
