from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:

        n = len(seats)
        max_distance = 1
        current_distance = 1

        for i in range(1, n):
            prev = seats[i - 1]
            current = seats[i]

            if prev == 0:
                current_distance += 1

            if current == 1:
                max_distance = max(max_distance, current_distance)
                current_distance = 1

        if seats[0] == 1 and seats[-1] == 1:
            return max_distance // 2

        max_left = 0
        max_right = 0
        if seats[0] == 0:
            max_left = 1
            for i in range(1, n):
                if seats[i] != 1:
                    max_left += 1
                else:
                    break

        if seats[-1] == 0:
            max_right = 1
            for i in range(n - 2, 0, -1):
                if seats[i] != 1:
                    max_right += 1
                else:
                    break
        return max(max_left, max_right, max_distance // 2)
