class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        more_than_ten = False

        num1_pointer = len(num1) - 1
        num2_pointer = len(num2) - 1

        result = []
        while num1_pointer >= 0 or num2_pointer >= 0:

            _num1 = ord(num1[num1_pointer]) - ord("0") if num1_pointer >= 0 else 0
            _num2 = ord(num2[num2_pointer]) - ord("0") if num2_pointer >= 0 else 0
            _result = _num1 + _num2

            if more_than_ten:
                _result += 1
                more_than_ten = False

            if _result >= 10:
                more_than_ten = True
                _result = _result % 10

            result.append(str(_result))

            num1_pointer -= 1
            num2_pointer -= 1

        if more_than_ten:
            result.append("1")

        return "".join(reversed(result))
