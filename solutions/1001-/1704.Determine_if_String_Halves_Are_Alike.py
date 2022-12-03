class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        s = s.lower()
        vovels = {'a', 'e', 'i', 'o', 'u'}
        vovels_a, vovels_b = 0, 0

        for i in range(len(s) // 2):

            a = s[i]
            b = s[len(s)-i-1]

            if a in vovels:
                vovels_a += 1
            if b in vovels:
                vovels_b += 1

        return vovels_a == vovels_b
