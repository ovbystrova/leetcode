from typing import List


class Solution:

    def checkIfExist(self, arr: List[int]) -> bool:

        cache = {}

        if len(arr) < 1:
            return False

        for i in range(len(arr)):

            if arr[i] % 2 != 0:
                if arr[i] * 2 in cache:
                    return True
                cache[arr[i]] = None

            elif (arr[i] / 2) in cache or (arr[i] * 2) in cache:
                return True
            cache[arr[i]] = None

        return False
