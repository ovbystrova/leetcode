from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        points_sorted = sorted(points, key=lambda x: x[1])
        min_arrow_shots = len(points_sorted)

        left, right = points_sorted[0][0], points_sorted[0][1]
        for point in points_sorted[1:]:
            _left = point[0]
            _right = point[1]

            if _left <= right:
                min_arrow_shots -= 1
                continue

            right = _right
            continue

        return min_arrow_shots
