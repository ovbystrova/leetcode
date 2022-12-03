from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        heights_sorted = sorted(heights)

        count_mismatch = 0

        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                count_mismatch += 1

        return count_mismatch
