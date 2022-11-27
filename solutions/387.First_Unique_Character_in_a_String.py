class Solution:
    """
    Time complexity O(n)
    Space complexity O(1)
    """
    def firstUniqChar(self, s: str) -> int:

        cache_once = {}
        cache_more_than_once = {}

        for i in range(len(s)):
            letter = s[i]
            if letter in cache_more_than_once:
                continue
            elif letter in cache_once:
                cache_more_than_once[letter] = i
                del cache_once[letter]
            else:
                cache_once[letter] = i

        if len(cache_once) == 0:
            return -1
        return list(cache_once.values())[0]