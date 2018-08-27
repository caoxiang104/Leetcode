"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
"""


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j].isdigit():
                    temp1 = [board[k][j] for k in range(9) if k != i]
                    temp2 = board[i][:]
                    temp2[j] = -1
                    if board[i][j] in temp1 or board[i][j] in temp2:
                        return False
                    else:
                        for m in range((i // 3) * 3, (i // 3 + 1) * 3):
                            for n in range((j // 3) * 3, (j // 3 + 1) * 3):
                                if board[i][j] == board[m][n] and i != m and j != n:
                                    return False
        return True


s = Solution()
array = [[".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]]
print(s.isValidSudoku(array))
