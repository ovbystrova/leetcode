from typing import List

class Solution:
    empty_symbol = "."

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            if not self._check_array(board[i]):
                return False
            if not self._check_column(board, i):
                return False
            if not self._check_square(board):
                return False

        return True

    def _check_array(self, nums) -> bool:
        """
        Check whether there are unique elements in nums
        """
        cache = []
        for i in range(len(nums)):
            if nums[i] in cache and nums[i] != self.empty_symbol:
                return False
            cache.append(nums[i])
        return True

    def _check_column(self, board, i):
        """
        Wrapper-function over self._check_array. Treat every column as an array.
        """
        column = [x[i] for x in board]
        return self._check_array(column)

    def _check_square(self, board):
        """
        Check where in a 3x3 square there are only uniqie values
        """
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                if not self._check_array(square):
                    return False
        return True
