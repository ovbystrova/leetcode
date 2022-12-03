class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left, right = 0, num

        while left <= right:

            mid = (left + right) // 2
            mid_square = mid * mid

            if mid_square == num:
                return True

            if mid * mid > num:
                right = mid - 1
            else:
                left = mid + 1

        return False
