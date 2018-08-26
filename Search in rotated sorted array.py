# -*- coding:utf-8 -*-
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
(例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2])。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
"""


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if nums[-1] < target < nums[0]:
            return -1
        if target == nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[0]:
            low = 1
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    high = mid - 1
                elif target > nums[mid] and nums[mid] < nums[0]:
                    high = mid - 1
                else:
                    low = mid + 1
            return - 1
        else:
            low = 1
            high = len(nums) - 1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    low = mid + 1
                elif target < nums[mid] and nums[mid] > nums[-1]:
                    low = mid + 1
                else:
                    high = mid - 1
            return - 1


s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 0))