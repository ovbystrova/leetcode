from typing import List

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:

        # Are the points unique? Spoiler: No
        set_points = set([(point[0], point[1]) for point in points])
        if len(set_points) == 1:
            return True

        # Find Dividing Line x
        xs = sorted([point[0] for point in set_points])
        x_line = (xs[-1] + xs[0]) / 2

        # Check That every point has reflection
        for point in points:
            x, y = point
            if x == x_line:
                continue
            x_reflection = x_line + (x_line - x)
            if (x_reflection, y) not in set_points:
                return False

        return True
