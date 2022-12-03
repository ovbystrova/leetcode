class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:

        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False

        word1_counter, word2_counter = {}, {}

        for i in range(len(word1)):
            word1_counter = self._update_counter(
                word1[i],
                word1_counter
            )
            word2_counter = self._update_counter(
                word2[i],
                word2_counter
            )
        if sorted(list(word1_counter.values())) != sorted(list(word2_counter.values())):
            return False
        return True

    def _update_counter(self, item, counter):
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 1
        return counter