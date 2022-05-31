from typing import List


class Solution:
    cache = {
        0: [1],
        1: [1, 1]
    }

    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex in Solution.cache:
            return Solution.cache[rowIndex]

        previous_line = self.getRow(rowIndex - 1)

        current_line = [1, 1]
        for i in range(1, len(previous_line)):
            current_line.insert(i, previous_line[i - 1] + previous_line[i], )

        Solution.cache[rowIndex] = current_line

        return current_line
