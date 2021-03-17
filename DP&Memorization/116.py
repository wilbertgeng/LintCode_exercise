"""116. Jump Game"""
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        n = len(A)
        dp = [False] * n
        dp[0] = True

        for i in range(n):
            for j in range(i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True 
                    break
        return dp[-1]
