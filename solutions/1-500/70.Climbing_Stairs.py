class Solution:
    cache = {
        1: 1,
        2: 2,
        3: 3
    }

    def climbStairs(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]

        ways_to_climb = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        Solution.cache[n] = ways_to_climb

        return ways_to_climb
