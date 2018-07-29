# -*- coding:utf-8 -*-
"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.
与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        min_value = float("Inf")
        min_abs = float("Inf")
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            while low < high:
                if nums[low] + nums[high] + nums[i] == target:
                    return target
                elif nums[low] + nums[high] + nums[i] < target:
                    temp = abs(nums[low] + nums[high] + nums[i] - target)
                    if temp < min_abs:
                        min_value = nums[low] + nums[high] + nums[i]
                        min_abs = temp
                    low += 1
                else:
                    temp = abs(nums[low] + nums[high] + nums[i] - target)
                    if temp < min_abs:
                        min_value = nums[low] + nums[high] + nums[i]
                        min_abs = temp
                    high -= 1
        return min_value


def main():
    s = Solution()
    print(s.threeSumClosest([-1, 2, 1,-4], 1))


if __name__ == '__main__':
    main()