"""
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
"""


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        temp = [i for i in range(1, n+1)]
        out = ""
        a = n - 1
        temp2 = 1
        k -= 1
        while temp:
            if a >= 1:
                for i in range(1, a+1):
                    temp2 *= i
            else:
                temp2 = 1
            a -= 1
            index = k // temp2
            if k >= temp2:
                k -= temp2 * (k // temp2)
            out += str(temp.pop(index))
            temp2 = 1
        return out


s = Solution()
print(s.getPermutation(3, 3))