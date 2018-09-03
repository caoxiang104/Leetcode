# -*- coding:utf-8 -*-
"""
给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3
输出:
[[ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]]
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        out = [[0] * n for i in range(n)]
        x = 0
        y = 0
        x_start = 0
        y_start = 0
        x_end = n - 1
        y_end = n - 1
        temp = 1  # 1 right 2 down 3 left 4 up
        count = 1
        while count <= n ** 2:
            if temp == 1:
                while y <= y_end:
                    out[x][y] = count
                    count += 1
                    if count > n ** 2:
                        return out
                    y += 1
                y -= 1
                x_start += 1
                x = x_start
                temp = 2
            if temp == 2:
                while x <= x_end:
                    out[x][y] = count
                    count += 1
                    if count > n ** 2:
                        return out
                    x += 1
                x -= 1
                y_end -= 1
                y = y_end
                temp = 3
            if temp == 3:
                while y >= y_start:
                    out[x][y] = count
                    count += 1
                    if count > n ** 2:
                        return out
                    y -= 1
                y += 1
                x_end -= 1
                x = x_end
                temp = 4
            if temp == 4:
                while x >= x_start:
                    out[x][y] = count
                    count += 1
                    if count > n ** 2:
                        return out
                    x -= 1
                x += 1
                y_start += 1
                y = y_start
                temp = 1
        return out


s = Solution()
print(s.generateMatrix(3))