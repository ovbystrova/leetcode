from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        if len(strs) <= 1:
            return 0

        column_counter = 0

        for i in range(len(strs[0])):

            column = [item[i] for item in strs]
            if column != sorted(column):
                column_counter += 1

        return column_counter
