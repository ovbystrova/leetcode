class Solution:
    def frequencySort(self, s: str) -> str:

        s_counter = {}
        s_new = []
        for i in range(len(s)):
            if s[i] in s_counter:
                s_counter[s[i]] += 1
            else:
                s_counter[s[i]] = 1
        s_counter = dict(sorted(s_counter.items(), key=lambda x: x[1], reverse=True))
        for letter, count in s_counter.items():
            s_new.append(letter * count)

        return "".join(s_new)