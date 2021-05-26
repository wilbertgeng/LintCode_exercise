"""116. Jump Game"""
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        m = len(A)

        dp = [False] * m
        dp[0] = True

        for i in range(1, m):
            for j in range(i):
                if j + A[j] >= i:
                    dp[i] = dp[j] or dp[i]
        return dp[-1]


        ###
        n = len(A)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break
        return dp[-1]
