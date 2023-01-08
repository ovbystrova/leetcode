class Solution:
    def reverseWords(self, s: str) -> str:

        start = end = 0
        new_string = ""

        for i in range(len(s)):

            if s[i] == " " or i == len(s) - 1:
                if i == len(s) - 1:
                    end += 1
                l = [x for x in s[start:end]][::-1]
                new_string += "".join(l)
                if i < len(s) - 1:
                    new_string += " "
                start = i + 1
                end = i + 1
                continue

            end += 1

        return new_string
