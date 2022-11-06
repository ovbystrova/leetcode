from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        intersection = []

        counter = Counter(nums1)
        for item in nums2:

            if counter[item] > 0:
                intersection.append(item)
                counter[item] -= 1

        return intersection
