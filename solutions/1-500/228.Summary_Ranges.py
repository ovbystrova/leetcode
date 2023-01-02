from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [f"{nums[0]}"]

        ranges = []

        start, end = nums[0], nums[0]

        for i in range(1, len(nums)):

            current = nums[i]
            previous = nums[i-1]

            if current - previous == 1:
                end = current
                if i == len(nums) - 1:
                    ranges.append(f"{start}->{end}")

            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}->{end}")
                if i == len(nums) - 1:
                    ranges.append(f"{current}")

                start = current
                end = current

        return ranges
