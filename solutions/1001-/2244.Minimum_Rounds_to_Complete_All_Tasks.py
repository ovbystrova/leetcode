from typing import List

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        difficulty_counter = dict()
        for task in tasks:
            if task in difficulty_counter:
                difficulty_counter[task] += 1
            else:
                difficulty_counter[task] = 1

        total_rounds = 0
        for task, count in difficulty_counter.items():
            if count < 2:
                return -1

            round_3 = count // 3
            rest = count % 3
            if rest == 1:
                round_3 -= 1
                round_2 = 2
            elif rest == 0:
                round_2 = 0
            else:
                round_2 = 1
            total_rounds += (round_3 + round_2)

        return total_rounds
