# -*- coding:utf-8 -*-
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
"""


# class Solution:
#     def trap(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         if len(height) == 0: return 0
#         left = []
#         sum_ = 0
#         temp_weight = 0
#         for index, weight in enumerate(height):
#             if not left:
#                 if weight != 0:
#                     left.append((weight, index))
#             else:
#                 if weight != 0 and weight < left[-1][0]:
#                     left.append((weight, index))
#                 elif weight == left[-1][0]:
#                     if index - left[-1][1] == 1:
#                         left.pop()
#                         left.append((weight, index))
#                     else:
#                         temp = left.pop()
#                         sum_ += (index - temp[1] - 1) * (temp[0] - temp_weight)
#                         temp_weight = temp[0]
#                         left.append((weight, index))
#                 elif weight != 0 and weight > left[-1][0]:
#                     while left:
#                         if weight >= left[-1][0]:
#                             temp = left.pop()
#                             if index - temp[1] == 1:
#                                 temp_weight = temp[0]
#                             else:
#                                 sum_ += (index - temp[1] - 1) * (temp[0] - temp_weight)
#                                 temp_weight = temp[0]
#                         else:
#                             sum_ += (index - left[-1][1] - 1) * (weight - temp_weight)
#                             temp_weight = weight
#                             break
#                     left.append((weight, index))
#                 else:
#                     left.append((weight, index))
#                     temp_weight = 0
#         return sum_


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0: return 0
        sum_ = 0
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        while left <= right:
            if left_max < right_max:
                if height[left] > left_max:
                    left_max = height[left]
                else:
                    sum_ += left_max - height[left]
                left += 1
            else:
                if height[right] > right_max:
                    right_max = height[right]
                else:
                    sum_ += right_max - height[right]
                right -= 1
        return sum_


s = Solution()
print(s.trap([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]))