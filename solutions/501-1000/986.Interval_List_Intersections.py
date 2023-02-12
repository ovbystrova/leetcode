from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        if len(firstList) == 0 or len(secondList) == 0:
            return []

        result = []

        first_pointer = 0
        second_pointer = 0

        while first_pointer < len(firstList) and second_pointer < len(secondList):

            first = firstList[first_pointer]
            second = secondList[second_pointer]

            _max = max(first[0], second[0])
            _min = min(first[1], second[1])

            if _max <= _min:
                result.append([_max, _min])

            if first[1] < second[1]:
                first_pointer += 1
            else:
                second_pointer += 1

        return result
