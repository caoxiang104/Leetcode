"""
实现 pow(x, n) ，即计算 x 的 n 次幂函数。
"""


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n < 0:
            return 1.0 / self.myPow(x, -n)
        else:
            if n % 2 == 1:
                return x * self.myPow(x * x, n // 2)
            else:
                return self.myPow(x * x, n // 2)


s = Solution()
print(s.myPow(2.01, 10))
