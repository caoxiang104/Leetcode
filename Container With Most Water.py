# -*- coding:utf-8 -*-
"""
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
输入: [1,8,6,2,5,4,8,3,7]
输出: 49
"""


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l_index = 0
        r_index = len(height) - 1
        max_value = (r_index - l_index) * min(height[l_index], height[r_index])
        low = 0
        high = len(height) - 1
        while low <= high:
            if height[low] <= height[high]:
                low += 1
                if low < r_index and height[low] > height[l_index]:
                    if (r_index - low) * min(height[low], height[r_index]) >= max_value:
                        max_value = (r_index - low) * min(height[low], height[r_index])
                        l_index = low
                    elif height[low] > height[r_index]:
                        l_index = low
            else:
                high -= 1
                if high > l_index and height[high] > height[r_index] :
                    if (high - l_index) * min(height[high], height[l_index]) >= max_value:
                        max_value = (high - l_index) * min(height[high], height[l_index])
                        r_index = high
                    elif height[high] > height[l_index]:
                        r_index = high
        return max_value


def main():
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))


if __name__ == '__main__':
    main()