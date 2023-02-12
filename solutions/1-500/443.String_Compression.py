from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:

        start = end = 0
        count = 1

        i = 1
        prev_item = chars[0]

        while i < len(chars):
            if prev_item == chars[i]:
                count += 1
                end += 1
                i += 1
                continue

            prev_item = chars[i]

            while end > start:
                chars.pop(end)
                end -= 1

            if count == 1:
                start = end = i
                i += 1
                continue

            counts = list(str(count))
            for count_symbol in counts:
                end += 1
                chars.insert(end, count_symbol)

            count = 1
            i = end + 2
            start = i - 1
            end = i - 1

        while end > start:
                chars.pop(end)
                end -= 1

        if count != 1:
            counts = list(str(count))
            for count_symbol in counts:
                end += 1
                chars.insert(end, count_symbol)

        return len(chars)
