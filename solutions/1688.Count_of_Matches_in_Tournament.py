class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_games = 0
        while n > 1:
            if n % 2 == 0:  # even
                total_games += n / 2
                n = n / 2

            else:
                total_games += (n - 1) / 2
                n = (n - 1) / 2 + 1
        return total_games
