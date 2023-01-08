from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        if len(gas) == 1:
            return 0

        min_total = sum(gas)  + sum(cost)
        min_id = 0
        total = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < min_total:
                min_id = i
                min_total = total

        if total < 0:
            return -1
        return (min_id + 1) % len(gas)
