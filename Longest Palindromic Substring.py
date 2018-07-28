# -*- coding:utf-8 -*-
"""最长回文序列"""
"""
状态方程
f(i; j) = 1 if i == j
f(i; j) = 1 if S[i] = S[j] and j = i + 1 
f(i; j) = 1 if S[i] = S[j] and f(i + 1; j − 1) == 1 and  j > i + 1
"""

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[0] * n for i in range(n)]
        start_index = 0
        max_len = 1
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j]:
                    if i - j < 2:
                        dp[j][i] = 1
                    else:
                        if dp[j + 1][i - 1] == 1:
                            dp[j][i] = 1
                else:
                    dp[j][i] = 0
                if dp[j][i] == 1 and i - j + 1 > max_len:
                    max_len = i - j + 1
                    start_index = j
        return s[start_index:start_index + max_len]


def main():
    s = Solution()
    print(s.longestPalindrome("babadada"))


if __name__ == '__main__':
    main()