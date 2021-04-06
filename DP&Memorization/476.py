"""476 · Stone Game"""
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame(self, A):
        # write your code here
        if not A:
            return 0
        range_sum = self.rangeSum(A)
        n = len(A)
        dp = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for mid in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid + 1][j] + range_sum[i][j])

        return dp[0][n - 1]

    def rangeSum(self, A):
        m = len(A)

        range_sum = [[0] * m for _ in range(m)]

        for i in range(m):
            range_sum[i][i] = A[i]

        for i in range(m - 1):
            for j in range(i + 1, m):
                range_sum[i][j] = range_sum[i][j - 1] + A[j]

        return range_sum
