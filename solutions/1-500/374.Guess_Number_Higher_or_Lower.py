# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:

        low, high = 1, n
        pred = n // 2
        guess_feedback = guess(pred)

        while guess_feedback != 0:

            if guess_feedback == -1:
                high = pred - 1

            elif guess_feedback == 1:
                low = pred + 1

            pred = (low + high) // 2
            guess_feedback = guess(pred)

        return pred
