class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        if len(word) == 1:
            return True

        for i in range(1, len(word)):
            prev = word[i - 1]
            current = word[i]

            if prev.islower() and current.isupper():  # 'GooGle'
                return False

            elif current.islower() and word[:i].isupper() and i >= 2:  # 'GOOgle'
                return False

        return True
