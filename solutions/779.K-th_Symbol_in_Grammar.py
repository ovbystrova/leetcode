class Solution:
    cache = {
        (1, 1): 0,
        (2, 1): 0,
        (2, 2): 1
    }

    def kthGrammar(self, n: int, k: int) -> int:

        if (n, k) in Solution.cache:
            return Solution.cache[(n, k)]

        if k % 2 != 0:
            k_prev_idx = (k + 1) / 2
        else:
            k_prev_idx = k / 2 if k > 2 else 1

        k_prev = self.kthGrammar(n - 1, k_prev_idx)

        if k_prev == 0:
            k_th_element = 0 if k % 2 != 0 else 1
        else:
            k_th_element = 1 if k % 2 != 0 else 0

        Solution.cache[(n, k)] = k_th_element

        return k_th_element
