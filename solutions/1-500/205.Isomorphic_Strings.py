class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        counter_s = {}
        counter_t = {}

        for i in range(len(s)):
            if s[i] in counter_s:
                counter_s[s[i]].append(i)
            else:
                counter_s[s[i]] = [i]
            if t[i] in counter_t:
                counter_t[t[i]].append(i)
            else:
                counter_t[t[i]] = [i]

        if sorted(list(counter_s.values())) != sorted(list(counter_t.values())):
            return False

        return True
