from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        i = len(asteroids) - 1
        while i >= 0:

            left_opposite = (i != 0) and ((asteroids[i-1] > 0) and (asteroids[i] < 0))
            if left_opposite:
                if abs(asteroids[i-1]) > abs(asteroids[i]):
                    asteroids.pop(i)
                    i -= 1
                elif abs(asteroids[i-1]) == abs(asteroids[i]):
                    asteroids.pop(i)
                    asteroids.pop(i-1)
                    i -= 2
                else:
                    asteroids.pop(i-1)
                    i -=1
                continue

            right_opposite = (i != len(asteroids) - 1) and ((asteroids[i+1] < 0) and (asteroids[i] > 0))
            if right_opposite:
                if abs(asteroids[i+1]) > abs(asteroids[i]):
                    asteroids.pop(i)
                    i -= 1
                elif abs(asteroids[i+1]) == abs(asteroids[i]):
                    asteroids.pop(i+1)
                    asteroids.pop(i)
                    i -= 1
                else:
                    asteroids.pop(i+1)
                continue

            i -= 1

        return asteroids
