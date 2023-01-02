class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split(" ")

        letter2word = {}
        values = set()

        if len(words) != len(pattern):
            return False

        for i, letter in enumerate(pattern):
            word = words[i]

            if letter not in letter2word:
                if word in values:
                    return False
                letter2word[letter] = word
                values.add(word)
                continue

            elif word != letter2word[letter]:
                return False

        return True
