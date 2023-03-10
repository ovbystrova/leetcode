from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        position = (len(nums1) + len(nums2)) // 2
        even_lenght = (len(nums1) + len(nums2)) % 2  == 0

        result = []

        pointer_1 = 0
        pointer_2 = 0

        while pointer_1 < len(nums1) and pointer_2 < len(nums2) and len(result) < position + 1:

            if nums1[pointer_1] <= nums2[pointer_2]:
                result.append(nums1[pointer_1])
                pointer_1 += 1
            else:
                result.append(nums2[pointer_2])
                pointer_2 += 1

        result.extend(nums1[pointer_1:])
        result.extend(nums2[pointer_2:])

        if even_lenght:
            return (result[position] + result[position-1]) / 2
        else:
            return  result[position]
