from typing import List

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        ### Approach 1: Greedy
        # if len(costs) == 0:
        #     return 0

        # total_ice_creams = 0
        # costs.sort()

        # min_ice_cream = costs[0]

        # while coins > 0 and len(costs) > 0 and min_ice_cream <= coins:
        #     total_ice_creams += 1
        #     del costs[0]
        #     coins -= min_ice_cream
        #     if len(costs) == 0:
        #         break
        #     min_ice_cream = costs[0]

        # return total_ice_creams

        ### Approach 2: Counting Sort

        costs_count = {}
        total_iceream = 0

        for cost in costs:
            if cost in costs_count:
                costs_count[cost] += 1
            else:
                costs_count[cost] = 1

        for i in range(1, max(costs_count.keys()) + 1):
            if i not in costs_count:
                continue

            if i > coins:
                break

            ice_creams = min(coins // i, costs_count[i])
            total_iceream += ice_creams
            coins -= i * ice_creams

        return total_iceream
