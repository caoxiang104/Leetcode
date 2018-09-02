# -*- coding:utf-8 -*-
"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
判断你是否能够到达最后一个位置。
"""


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0 or len(nums) == 1: return True
        i = 0
        max_len = 0
        start_point = 0
        while i <= len(nums) - 1:
            if nums[i] == 0:
                return False
            if i + nums[i] >= len(nums) - 1:
                return True
            for j in range(i + 1, i + nums[i] + 1):
                if j + nums[j] >= len(nums) - 1:
                    return True
                elif j + nums[j] > max_len:
                    max_len = j + nums[j]
                    start_point = j
            i = max(i + 1, start_point + 1)
        return False


s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))