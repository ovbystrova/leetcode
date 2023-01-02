from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if len(strs) == 1:
            return [strs]

        result = {}

        for item in strs:
            item_sorted = "".join(sorted(item))

            if item_sorted  not in result:
                result[item_sorted] = [item]
            else:
                result[item_sorted].append(item)

        return list(result.values())
