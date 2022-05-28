from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        number_of_zeros = arr.count(0)

        if number_of_zeros != 0:

            for i in range(1, len(arr)):

                if arr[i - 1] != 0:
                    # print(f"Previous element {arr[i-1]} != 0. Continue")
                    continue

                if arr[max(i - 2, 0):i] == [0, 0] and arr[:i].count(0) % 2 == 0:
                    # print(f"Just did it. i-1={arr[i-1]} i={arr[i]}Continue")
                    continue

                # arr[i-1] = 0
                # print(f"Array Before: {arr}")
                tmp = arr[i]
                arr[i] = 0
                # print(f"Array Before (with zero): {arr}")
                for j in range(i + 1, len(arr)):
                    to_next = arr[j]
                    arr[j] = tmp
                    tmp = to_next
                    # print(f"To_next {to_next}: Tmp{tmp}. Arr: {arr}")
                # print(f"Array After: {arr}")

