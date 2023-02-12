class Solution:

    cache = {
        0: 0,
        1: 1,
        2: 1
    }

    def tribonacci(self, n: int) -> int:

        if n in self.cache:
            return self.cache[n]

        self.cache[n] = self.tribonacci(n-3) + self.tribonacci(n-2) + self.tribonacci(n-1)

        return self.cache[n]
