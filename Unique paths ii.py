"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""


class Solution:
    def __init__(self):
        self.count = 0

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0]*n for i in range(m)]
        if obstacleGrid[0][0] != 1:
            dp[0][0] = 1
        else:
            return 0
        for i in range(1, m):
            if obstacleGrid[i][0] != 1:
                if obstacleGrid[i - 1][0] == 1:
                    dp[i][0] = 0
                else:
                    dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
        for i in range(1, n):
            if obstacleGrid[0][i] != 1:
                if obstacleGrid[0][i - 1] == 1:
                    dp[0][i] = 0
                else:
                    dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] != 1:
                    if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                        dp[i][j] = 0
                    elif obstacleGrid[i - 1][j] == 1:
                        dp[i][j] = dp[i][j - 1]
                    elif obstacleGrid[i][j - 1] == 1:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0
        return dp[m - 1][n - 1]


s = Solution()
print(s.uniquePathsWithObstacles([[0,1]]))