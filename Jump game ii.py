# -*- coding:utf-8 -*-
"""
给定一个非负整数数组，你最初位于数组的第一个位置。
数组中的每个元素代表你在该位置可以跳跃的最大长度。
你的目标是使用最少的跳跃次数到达数组的最后一个位置。
"""


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)
        if n == 0 or n == 1: return 0
        i = 0
        max_len = 0
        next_point = 0
        while i < n:
            if i == n - 1:
                break
            if i + nums[i] >= n - 1:
                count += 1
                break
            candidates = nums[i + 1:i + nums[i] + 1]
            for j in range(len(candidates)):
                if candidates[j] + (i + j + 1) >= n - 1:
                    count += 2
                    return count
                if candidates[j] + (i + j + 1) >= max_len:
                    max_len = candidates[j] + (i + j + 1)
                    next_point = j
            i += next_point + 1
            count += 1
        return count


s = Solution()
print(s.jump([5, 4, 0, 1, 3, 6, 8, 0, 9, 4, 9, 1, 8, 7, 4, 8]))