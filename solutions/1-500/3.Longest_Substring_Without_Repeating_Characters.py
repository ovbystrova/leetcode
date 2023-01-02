class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start_idx = 0
        longest = 0
        symbol2id = {}

        for end_idx in range(len(s)):
            if s[end_idx] in symbol2id:
                start_idx = max(symbol2id[s[end_idx]], start_idx)

            longest = max(longest, end_idx - start_idx + 1)
            symbol2id[s[end_idx]] = end_idx + 1

        return longest
