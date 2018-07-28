# -*- coding:utf-8 -*-
"""
输入: s = "PAYPALISHIRING", numRows = 4
输出: "PINALSIGYAHRPI"
解释:

P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        temp = list(s[::-1])
        n = len(s)
        str = ""
        if n == 0 or n == 1 or numRows == 1:
            return s
        dp = [[] for i in range(numRows)]
        for j in range(n):
            for i in range(numRows):
                if not temp:
                    for i in range(numRows):
                        str += "".join(dp[i])
                        if i != numRows - 1:
                            str += "\n"
                    return str
                if j % (numRows-1) == 0 or j == 0:
                    dp[i].append(temp.pop())
                elif j % (numRows-1) + i + 1 == numRows:
                    dp[i].append(temp.pop())
                else:
                    dp[i].append(" ")



def main():
    s= Solution()
    print(s.convert("ABafsgdfgdfgdgdf", 3))


if __name__ == '__main__':
    main()