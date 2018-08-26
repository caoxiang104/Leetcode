"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
你的算法时间复杂度必须是 O(log n) 级别。
如果数组中不存在目标值，返回 [-1, -1]。
输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
"""


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        low = self.binarySort(nums, target - 0.5)
        high = self.binarySort(nums, target + 0.5)
        if low == high:
            return [-1, -1]
        else:
            return [low + 1, high]

    def binarySort(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return high


s = Solution()
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))