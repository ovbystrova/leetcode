from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        answer = set()

        nums1_set = set(nums1)
        
        for item in nums2:
            if item in nums1_set:
                answer.add(item)

        return list(answer)
