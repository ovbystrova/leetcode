from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        if len(arr) <= k:
            print(f"Return since k < {len(arr)}: {arr}")
            return arr

        if x < arr[0]:  # We don't have x in array so return the first k elements
            print(f"Return first {k} elements: {arr[:k]}")
            return arr[:k]

        elif x > arr[-1]:  # We don't have x in array so return the last k elements
            print(f"Return lst {k} elements: {arr[:k]}")
            return arr[-k:]

        left, right = 0, len(arr) - k

        while left < right:

            # mid_id = left + (right - left)//2
            mid_id = (right + left) // 2
            mid_value = arr[mid_id]

            if x - mid_value > arr[mid_id + k] - x:
                left = mid_id + 1
            else:
                right = mid_id

        return arr[left: left + k]