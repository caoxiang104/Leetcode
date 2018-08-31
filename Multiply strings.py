# -*- coding:utf-8 -*-
"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        n = n1 + n2
        result = [0] * n
        for idx1, value1 in enumerate(num1):
            for idx2, value2 in enumerate(num2):
                result[idx1 + idx2] += int(value1) * int(value2)
        for i in range(n - 1):
            if result[i] > 9:
                result[i + 1] += result[i] // 10
                result[i] = result[i] % 10
        if result[-1] == 0:
            return "".join(map(str, result[:-1][::-1]))
        else:
            return "".join(map(str, result[::-1]))


s = Solution()
print(s.multiply("123", "456"))