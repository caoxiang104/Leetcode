# -*- coding:utf-8 -*-
"""
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
"""


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        nums = list(filter(lambda x: x > 0, nums))
        if not nums:
            return 1
        min_num = min(nums)
        nums = list(set(nums))
        n = len(nums)
        if min_num != 1:
            return 1
        else:
            for i in range(n):
                if nums[i] <= n and nums[i] - 1 <= i:
                    temp = nums[i] - 1
                    nums[i], nums[temp] = nums[temp], nums[i]
            for i in range(len(nums)):
                if nums[i] != i + 1:
                    return i+1
            return nums[-1] + 1


s = Solution()
print(s.firstMissingPositive([9,4,5,-3,-2,-1,-9,1,1,6,-4,-9]))