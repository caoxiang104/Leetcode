# -*- coding:utf-8 -*-
"""
给定一个没有重复数字的序列，返回其所有可能的全排列。
"""


class Solution:
    def __init__(self):
        self.str = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        self.recurse(nums, n, 0, [])
        return self.str

    def recurse(self, nums, n, cur_len, temp_list):
        if cur_len == n:
            self.str.append(temp_list)
            return
        for i in range(len(nums)):
            self.recurse(nums[:i] + nums[i + 1:], n, cur_len + 1, temp_list + [nums[i]])


s = Solution()
print(s.permute([1, 2, 3]))