from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(_) for _ in digits]
        number = "".join(digits)
        number = int(number)
        number += 1

        number_string = str(number)

        return list(number_string)