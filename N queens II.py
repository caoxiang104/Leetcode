# -*- coding:utf-8 -*-
"""
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
"""


class Solution:
    def __init__(self):
        self.count = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(n):
            self.find_solve(n, [i])
        return self.count

    def find_solve(self, n, sol):
        if len(sol) == n:
            self.count += 1
            return
        for y in range(n):
            if self.ident(sol, len(sol), y):
                if self.find_solve(n, sol):
                    return True
            self.undo(sol, n)
        return False

    def ident(self, sol, x, y):
        sol.append(y)
        for i in range(len(sol) - 1):
            if sol[i] == y or abs(x - i) == abs(y - sol[i]):
                return False
        return True

    def undo(self, sol, n):
        sol.pop()