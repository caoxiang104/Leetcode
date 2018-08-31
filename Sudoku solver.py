class Solution:
    def __init__(self):
        self.val = dict()
        self.ret = dict()
        self.board = []

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        point_sets = "123456789"
        self.board = board
        for i in range(9):
            self.val[('row', i)] = ""
            self.val[('col', i)] = ""
        for i in range(3):
            for j in range(3):
                self.val[(i, j)] = ""
        for idx, datas in enumerate(board):
            for idy, data in enumerate(datas):
                if board[idx][idy] != '.':
                    self.val[('row', idx)] += data
                    self.val[('col', idy)] += data
                    self.val[(idx // 3, idy // 3)] += data
                else:
                    self.ret[(idx, idy)] = []
        for idx, idy in self.ret.keys():
            self.ret[(idx, idy)] = [value for value in point_sets if value not in (self.val[('row', idx)] +
                                                                                   self.val['col', idy] + self.val[(idx // 3, idy // 3)])]
        self.find_solve()

    def find_solve(self):
        if len(self.ret) == 0:
            return True
        idx, idy = min(self.ret, key=lambda x:len(self.ret[x]))
        for value in self.ret[(idx, idy)]:
            update = {(idx, idy): self.ret[(idx, idy)]}
            if self.ident(value, idx, idy, update):
                if self.find_solve():
                    return True
            self.undo(idx, idy, update)
        return False

    def ident(self, value, idx, idy, update):
        self.board[idx][idy] = value
        self.ret.pop((idx, idy))
        for i, j in self.ret.keys():
            if (i == idx or j == idy or (i // 3, j // 3) == (idx // 3, idy // 3)) \
                    and value in self.ret[(i, j)]:
                update[(i, j)] = value
                self.ret[(i, j)].remove(value)
                if len(self.ret[(i, j)]) == 0:
                    return False
        return True

    def undo(self, idx, idy, update):
        self.board[idx][idy] = '.'
        for key in update.keys():
            if key in self.ret.keys():
                self.ret[key].extend(update[key])
            else:
                self.ret[key] = update[key]
        return None


s = Solution()
solver = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
          ["7", ".", ".", ".", ".", ".", ".", ".", "."],
          [".", "2", ".", "1", ".", "9", ".", ".", "."],
          [".", ".", "7", ".", ".", ".", "2", "4", "."],
          [".", "6", "4", ".", "1", ".", "5", "9"," ."],
          [".", "9", "8", ".", ".", ".", "3", ".", "."],
          [".", ".", ".", "8", ".", "3", ".", "2", "."],
          [".", ".", ".", ".", ".", ".", ".", ".", "6"],
          [".", ".", ".", "2", "7", "5", "9", ".", "."]]
s.solveSudoku(solver)
print(solver)