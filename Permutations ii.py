# -*- coding:utf-8 -*-
"""
给定一个可包含重复数字的序列，返回所有不重复的全排列。
"""


class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return []
        self.recurse(nums, n, 0, [])
        return self.res

    def recurse(self, nums, n, cur_len, temp_list):
        if n == cur_len:
            self.res.append(temp_list)
        num_set = set()
        for i in range(len(nums)):
            if nums[i] in num_set:
                continue
            else:
                num_set.add(nums[i])
                self.recurse(nums[:i] + nums[i + 1:], n, cur_len + 1, temp_list + [nums[i]])


s = Solution()
print(s.permuteUnique([1, 1, 2]))