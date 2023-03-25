from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        count_planted = 0

        for i in range(len(flowerbed)):

            current = flowerbed[i]
            if current != 0:
                continue

            empty_left = (i == 0) or (flowerbed[i-1] == 0)
            empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

            if empty_left and empty_right:
                count_planted += 1
                flowerbed[i] = 1

        return count_planted >= n
