class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time complexity O(len(s))
        Space complexity O(1)
        :param s:
        :param t:
        :return:
        """

        if len(s) != len(t):
            return False

        cache_s = {}
        cache_t = {}

        for i in range(len(s)):
            if s[i] not in cache_s:
                cache_s[s[i]] = 1
            else:
                cache_s[s[i]] += 1
            if t[i] not in cache_t:
                cache_t[t[i]] = 1
            else:
                cache_t[t[i]] += 1

        if len(cache_s) != len(cache_t):
            return False

        for key, value in cache_s.items():

            if key not in cache_t:
                return False

            elif cache_t[key] != value:
                return False

        return True
