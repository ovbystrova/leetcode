# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:

        if n == 1:
            return 1

        left, right = 0, n

        while left < right:

            mid = (left + right) // 2

            is_next_bad = isBadVersion(mid + 1)

            if is_next_bad:

                is_current_bad = isBadVersion(mid)
                if is_current_bad:
                    right = mid
                else:
                    return mid + 1
            else:
                left = mid