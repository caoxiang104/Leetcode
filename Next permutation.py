# -*- coding:utf-8 -*-
"""
实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。
如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
必须原地修改，只允许使用额外常数空间。
以下是一些例子，输入位于左侧列，其相应输出位于右侧列。
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        num = nums[-1]
        index = len(nums) - 2
        while index >= 0:
            if num > nums[index]:
                k = index + 1
                while k + 1 < len(nums) and nums[k + 1] > nums[index]:
                    k += 1
                nums[index], nums[k] = nums[k], nums[index]
                break
            else:
                num = nums[index]
            index -= 1
        i = index + 1
        j = len(nums) - 1
        while i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


s = Solution()
nums = [1, 3, 2]
print(s.nextPermutation(nums))
print(nums)