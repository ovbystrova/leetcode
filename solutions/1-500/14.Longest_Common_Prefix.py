from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        i = 0 
        min_length = min([len(s) for s in strs])

        while i < min_length:
            symbol = strs[0][i]

            for j in range(1, len(strs)):
                if strs[j][i] != symbol:
                    return strs[0][:i]

            i += 1

        return strs[0][:i]
