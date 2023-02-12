class Solution:
    def isValid(self, s: str) -> bool:

        open_brackets =  ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        open2close = {open_b: close_b for open_b, close_b in zip(
           open_brackets,
            close_brackets
        )}

        stack = []
        for symbol in s:
            if symbol in open2close:
                stack.append(symbol)
                continue
            if len(stack) == 0:
                return False
            elif open2close[stack[-1]] != symbol:
                return False
            stack.pop(-1)

        if len(stack) > 0:
            return False

        return True
