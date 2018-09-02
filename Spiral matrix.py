# -*- coding:utf-8 -*-
"""
给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
示例 1:
输入:
[[ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]]
输出: [1,2,3,6,9,8,7,4,5]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        temp = 1  # 1 right 2 down 3 up 4 down
        m = len(matrix)
        res = []
        if m == 0: return []
        n = len(matrix[0])
        if m == 1: return matrix[0]
        if n == 1:
            for i in range(m):
                res.append(matrix[i][0])
            return res
        start_x = 0
        start_y = 0
        end_x = m - 1
        end_y = n - 1
        x, y = 0, 0
        while len(res)!=n*m:
            if temp == 1:
                while y <= end_y:
                    if len(res) == n*m:
                        return res
                    res.append(matrix[x][y])
                    y += 1
                start_x += 1
                temp = 2
                x = start_x
                y -= 1
            if temp == 2:
                while x <= end_x:
                    if len(res) == n*m:
                        return res
                    res.append(matrix[x][y])
                    x += 1
                end_y -= 1
                temp = 3
                y = end_y
                x -= 1
            if temp == 3:
                while y >= start_y:
                    if len(res) == n*m:
                        return res
                    res.append(matrix[x][y])
                    y -= 1
                end_x -= 1
                temp = 4
                x = end_x
                y += 1
            if temp == 4:
                while x >= start_x:
                    if len(res) == n*m:
                        return res
                    res.append(matrix[x][y])
                    x -= 1
                start_y += 1
                temp = 1
                y = start_y
                x += 1
        return res


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))