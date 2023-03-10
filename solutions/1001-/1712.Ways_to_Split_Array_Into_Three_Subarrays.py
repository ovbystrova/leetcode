from typing import List

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:

        result = 0

        # Create prefix summ array
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        total = prefix_sum[-1]

        # For every potential first pointer get acceptable middle pointers
        for first_pointer in range(len(prefix_sum) - 1):

            if prefix_sum[first_pointer] > total - prefix_sum[first_pointer]:
                # we cannot create a good split
                continue
            min_second_pointer = self._find_min_max_second_pointer(
                first_pointer,
                prefix_sum,
                mode="min"
            )
            max_second_pointer = self._find_min_max_second_pointer(
                first_pointer,
                prefix_sum,
                mode="max"
            )

            if min_second_pointer is None or max_second_pointer is None:
                continue
            result += max_second_pointer - min_second_pointer + 1

        return result % 1_000_000_007

    def _find_min_max_second_pointer(self, first_pointer, prefix_sum, mode):

        second_pointer = None
        left_summ = prefix_sum[first_pointer]  # constant because we already have first pointer

        left, right = first_pointer, len(prefix_sum) - 1
        switch_id = -1 if mode == "min" else 1
        # Stoping criteria: if left_summ <= mid_summ <= right_summ and id + swith_id make it False

        while left < right:
            mid_id = left + (right - left) // 2
            right_summ = prefix_sum[-1] - prefix_sum[mid_id]
            mid_summ = prefix_sum[-1] - (left_summ + right_summ)

            if mid_summ < left_summ:
                left = mid_id + 1
                continue

            elif mid_summ > right_summ:
                right = mid_id
                continue

            else:  # (left_summ <= mid_summ <= right_summ): we found valid second pointer, check whether it is the minum / maximum valid or just a valid one
                new_id = mid_id + switch_id
                new_right = prefix_sum[-1] - prefix_sum[new_id]
                new_mid = prefix_sum[-1] - (left_summ + new_right)
                if (new_id == first_pointer) or (new_id == len(prefix_sum) - 1):
                    # current mid_id is the closest to first_pointer or to the end of nums
                    return mid_id
                if mode == "min":
                    if left_summ > new_mid:  # new_id is not a valid second pointer
                        return mid_id
                    right = mid_id  # new_id is a valid second pointer; continue searching

                else:  # mode == "max"
                    if new_mid > new_right:  # new_id is not a valid second pointer
                        return mid_id
                    left = mid_id + 1  # new_id is a valid second pointer; continue searching

        return second_pointer
