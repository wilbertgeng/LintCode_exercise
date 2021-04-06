"""741 · Calculate Maximum Value II"""
class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def maxValue(self, str):
        # write your code here
        if not str:
            return 0

        n = len(str)

        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = int(str[i])
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for mid in range(i, j):
                    dp[i][j] = max(dp[i][j], dp[i][mid] * dp[mid + 1][j], dp[i][mid] + dp[mid + 1][j])

        return dp[0][n - 1]
