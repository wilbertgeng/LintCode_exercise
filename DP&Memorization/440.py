"""440. Backpack III
"""
class Solution:
    """
    @param A: an integer array
    @param V: an integer array
    @param m: An integer
    @return: an array
    """
    def backPackIII(self, A, V, m):
        # write your code here
        ## Practice:
        n = len(A)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j < A[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - A[i - 1]] + V[i - 1])
        return max(dp[-1])









        ####
        n = len(A)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(1, n + 1):
            for j in range(m + 1):
                if j < A[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - A[i - 1]] + V[i -1])

        return max(dp[n])
