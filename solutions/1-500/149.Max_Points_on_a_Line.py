from collections import Counter
from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        if len(points) == 1:
            return 1

        max_points_on_line = 1
        for i in range(len(points)-1):
            point_curr = points[i]
            slopes = Counter()
            max_points_for_i = 1
            for j in range(i+1, len(points)):
                point_next = points[j]
                x_diff = point_next[0] - point_curr[0]
                y_diff = point_next[1] - point_curr[1]
                if x_diff == 0:
                    k = f"{point_curr[0]}_x"
                elif y_diff == 0:
                    k = f"{point_curr[1]}_y"
                else:
                    k = y_diff / x_diff

                slopes[k] += 1
                max_points_for_i = max(max_points_for_i, 1 + slopes[k])

            max_points_on_line = max(max_points_on_line, max_points_for_i)
        return max_points_on_line
