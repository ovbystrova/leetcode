from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,5,1]
        # 3

        low_id, high_id = 0, len(nums) - 1  # 0, 6

        while low_id <= high_id:

            mid_id = (low_id + high_id) // 2  # 3
            mid_value = nums[mid_id]  # 7

            if target == mid_value:  # Если нашли нужный элемент
                return mid_id

            if target > mid_value:  # 3 > 5: False
                # Проверяем нужно ли делать реверс или нет.
                do_reverse = True if (nums[low_id] > mid_value) and (nums[low_id] <= target) else False  # True
                print(f"Do reverse : {do_reverse}. {nums[low_id]} > {mid_value}")
                if do_reverse:
                    high_id = mid_id - 1
                else:
                    low_id = mid_id + 1

            if target < mid_value:  # 3 < 5: True
                # Проверяем нужно ли делать реверс или нет.
                do_reverse = True if (nums[high_id] < mid_value) and (nums[high_id] >= target) else False  # False
                if do_reverse:
                    low_id = mid_id + 1  # low_id = 2
                else:
                    high_id = mid_id - 1

        return -1