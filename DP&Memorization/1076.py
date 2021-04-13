"""1076 · Minimum ASCII Delete Sum for Two Strings"""
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: the lowest ASCII sum of deleted characters to make two strings equal
    """
    def minimumDeleteSum(self, s1, s2):
        # Write your code here
        m = len(s1)
        n = len(s2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i][j - 1] + ord(s2[j - 1]), dp[i - 1][j] + ord(s1[i - 1]))

        return dp[-1][-1]
