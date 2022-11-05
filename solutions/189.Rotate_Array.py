class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def reverse(nums, i, j):
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

                i += 1
                j -= 1
            return nums

        if len(nums) <= 1:
            return

        n = len(nums)
        k = k % n

        if k == 0:
            return

        reverse(nums, 0, n - k - 1)
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - 1)
