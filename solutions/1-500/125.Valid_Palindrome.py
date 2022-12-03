from string import punctuation

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.translate(str.maketrans('', '', punctuation + " "))
        s = s.lower()

        if len(s) == 0:
            return True

        for i in range(len(s) // 2):

            if s[i] != s[len(s) - i - 1]:
                return False

        return True
