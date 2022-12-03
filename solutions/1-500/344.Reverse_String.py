from typing import List


# Time Complexity O(N), Space Complexity O(1)
class Solution:
    i = 0

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if self.i <= (len(s) - 1) // 2:
            s[self.i], s[-(self.i + 1)] = s[-(self.i + 1)], s[self.i]
            self.i += 1
            self.reverseString(s)
