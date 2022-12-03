from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        if arr[1] < arr[0]:
            return False

        get_pick = False

        for i in range(1, len(arr)):
            prev_element = arr[i - 1]

            if arr[i] == prev_element:
                return False

            elif arr[i] > prev_element:
                if not get_pick:
                    continue
                else:
                    return False

            elif arr[i] < prev_element:
                if not get_pick:
                    print(f"Found Peak {arr[i]}. Setting to True")
                    get_pick = True
                    continue
                continue

        if not get_pick:
            return False

        return True
