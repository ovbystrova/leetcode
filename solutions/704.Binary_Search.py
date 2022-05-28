from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low_id = 0
        high_id = len(nums) - 1

        while low_id <= high_id:

            _id = (low_id + high_id) // 2
            _el = nums[_id]

            if _el == target:
                return _id
            elif _el > target:
                high_id = _id - 1
            else:
                low_id = _id + 1

        return -1
