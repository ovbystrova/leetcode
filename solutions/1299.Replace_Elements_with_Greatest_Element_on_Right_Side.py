from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        if len(arr) == 1:
            arr[0] = -1
            return arr

        max_element = arr[-1]
        for i in range(len(arr) - 1, 0, -1):

            if arr[i] > max_element:
                tmp = arr[i]
                arr[i] = max_element
                max_element = tmp
            else:
                arr[i] = max_element

        arr[-1] = -1
        arr[0] = max_element

        return arr
