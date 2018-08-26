"""
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 找最长连续的子串
        stack = []
        out = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if stack:
                    out.append(stack.pop())
                    out.append(i)
        out.sort()
        sum_ = 1
        temp = 1
        for i in range(len(out) - 1):
            if out[i] == out[i + 1] - 1:
                temp += 1
                if temp > sum_:
                    sum_ = temp
            else:
                temp = 1
        return sum_


s = Solution()
print(s.longestValidParentheses(")()"))
