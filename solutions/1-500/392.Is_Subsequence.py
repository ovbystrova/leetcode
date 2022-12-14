class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True

        i = 0
        current_id = 0
        while i < len(t) and current_id < len(s):
            if s[current_id] == t[i]:
                i += 1
                current_id += 1
            else:
                i += 1

        if current_id == 0:
            return False

        if current_id == len(s):
            return True

        return False
