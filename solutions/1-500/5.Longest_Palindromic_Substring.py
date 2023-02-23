class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        start, end = 0, 0

        for i in range(len(s) - 1):
            left, right = self._expand_center(i, i, s)
            if right - left > end - start:
                start = left + 1
                end = right
            left, right = self._expand_center(i, i + 1, s)
            if right - left > end - start:
                start = left + 1
                end = right

        return s[start:end]

    def _expand_center(self, left, right, s):

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left, right
