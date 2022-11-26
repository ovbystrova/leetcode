class Solution:
    def reverse(self, x: int) -> int:

        max_value = 2 ** 31 - 1
        x_reversed = 0
        is_x_negative = x < 0
        x = abs(x)

        while x != 0:
            tmp = x % 10
            x = x // 10

            if (x_reversed > max_value / 10) or (x_reversed == max_value / 10 and tmp > 7):
                return 0

            x_reversed = x_reversed * 10 + tmp

        return -x_reversed if is_x_negative else x_reversed
