# -*- coding:utf-8 -*-
"""
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。
例如，给出 n = 3，生成结果为：
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n <= 0:
            return []
        res = []
        item = ""
        left = n #左括号个数
        right = n #右括号个数
        self.DFS(left, right, item, res)
        return res

    def DFS(self, left, right, item, res):
        if left > right:   # 保证左括号数大于右括号
            return
        if left == right == 0:  # 当且仅当左右括号数量都为0时，正常结束
            res.append(item)
        else:
            if left > 0:
                self.DFS(left-1, right, item+"(", res)  # 括号要想匹配，首先应该压入左括号，再压入右括号
            if right > 0:
                self.DFS(left, right-1, item+")", res)


def main():
    s = Solution()
    print(s.generateParenthesis(3))


if __name__ == '__main__':
    main()