# -*- coding:utf-8 -*-
"""
给定一个字符串 (s) 和一个字符模式 (p)。实现支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的元素。
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
"""


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dp(i, j):
            if (i, j) not in memo:
                if j == len(p):
                    ans = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p: return True
        if not p: return False
        if len(p) > 1 and p[1] == "*":
            if len(s) > 0 and (p[0] == s[0] or p[0] == "."):
                # ab 和 a* 或 ab 和 .*(. 为a或者不为a)
                return self.isMatch2(s[1:], p) or self.isMatch2(s, p[2:])
            else:
                # ab 和 b*
                return self.isMatch2(s, p[2:])
        if len(s) > 0 and (s[0] == p[0] or p[0] == "."):
            return self.isMatch2(s[1:], p[1:])
        return False


s = Solution()
print(s.isMatch("aaa","a*a"))