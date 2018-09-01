# -*- coding:utf-8 -*-
"""
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
"""


# class Solution:
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """
#         if len(s) == 0 and len(p) == 0:
#             return True
#         if len(p) == 0:
#             return False
#         if len(s) == 0:
#             for i in p:
#                 if i != "*":
#                     return False
#             return True
#         dp = [[0] * (len(p) + 1) for i in range(len(s) + 1)]
#         dp[0][0] = 1
#         for i in range(1, len(p)+1):
#             if dp[0][i - 1] == 1 and p[i - 1] == '*':
#                 dp[0][i] = 1
#         for i in range(1, len(s)+1):
#             for j in range(1, len(p)+1):
#                 if dp[i - 1][j - 1] == 1:
#                     if p[j - 1] == s[i - 1] or p[j - 1] == "?" or p[j - 1] == '*':
#                         dp[i][j] = 1
#                 elif dp[i - 1][j] == 1:
#                     if p[j - 1] == '*':
#                         dp[i][j] = 1
#                 elif dp[i][j - 1] == 1:
#                     if p[j - 1] == "*":
#                         dp[i][j] = 1
#         return dp[len(s)][len(p)]


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s = len(s)
        len_p = len(p)
        if len_s == 0 and len_p == 0:
            return True
        if len_s == 0:
            for i in p:
                if i != "*":
                    return False
            return True
        if len_p == 0:
            return False
        si = 0
        pi = 0
        last_s = 0
        last_p = -1
        while si < len_s:
            if pi < len_p and (s[si] == p[pi] or p[pi] == "?"):
                si += 1
                pi += 1
            elif pi < len_p and p[pi] == "*":
                last_s = si
                last_p = pi
                pi += 1
            elif last_p != -1:
                si = last_s + 1
                pi = last_p + 1
                last_s += 1
            else:
                return False
        while pi < len_p:
            if p[pi] == '*':
                pi += 1
        return pi == len_p


s = Solution()
print(s.isMatch("aa", "*"))