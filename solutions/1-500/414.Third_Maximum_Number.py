from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        _max, _max_second, _max_third = nums[0], None, None

        for i in range(1, len(nums)):

            if nums[i] == _max or nums[i] == _max_second or nums[i] == _max_third:
                continue

            if nums[i] > _max:
                _max_third = _max_second
                _max_second = _max
                _max = nums[i]
                continue

            elif _max_second is None:
                _max_second = nums[i]
                continue

            elif nums[i] > _max_second:
                _max_third = _max_second
                _max_second = nums[i]
                continue

            elif _max_third is None:
                _max_third = nums[i]
                continue

            elif nums[i] > _max_third:
                _max_third = nums[i]
                continue

        if _max_third is None:
            return _max

        return _max_third
