class Solution:
    cache = {}

    def fib(self, n: int) -> int:

        if n == 0:
            Solution.cache[n] = 0
            return 0

        elif n in [1, 2]:
            Solution.cache[n] = 1
            return 1

        if n in Solution.cache.keys():
            return Solution.cache[n]

        Solution.cache[n] = Solution.fib(self, n - 1) + Solution.fib(self, n - 2)

        return Solution.cache[n]
