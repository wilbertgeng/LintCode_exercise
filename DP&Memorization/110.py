"""110 · Minimum Path Sum"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        if not grid:
            return 0

        dp = list(grid)

        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]
