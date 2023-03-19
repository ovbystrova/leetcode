from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) == 1:
            return nums

        split_id = int(len(nums) / 2)

        list1 = nums[:split_id]
        list2 = nums[split_id:]

        list1 = self.sortArray(list1)
        list2 = self.sortArray(list2)

        return self._merge(list1, list2)


    def _merge(self, list1, list2):

        poinert_1 = pointer_2 = 0
        list_merged = []

        while poinert_1 < len(list1) and pointer_2 < len(list2):

            if list1[poinert_1] <= list2[pointer_2]:
                list_merged.append(list1[poinert_1])
                poinert_1 += 1

            else:
                list_merged.append(list2[pointer_2])
                pointer_2 += 1


        list_merged.extend(list1[poinert_1:])
        list_merged.extend(list2[pointer_2:])

        return list_merged
