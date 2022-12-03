from string import punctuation
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        paragraph = paragraph.lower()
        for punct in punctuation:
            paragraph = paragraph.replace(punct, ' ')

        words = paragraph.split()
        words = [word for word in words if word not in banned]
        c = Counter(words)
        return c.most_common(1)[0][0]
