"""92. Backpack
"""
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        dp = [0] * (m + 1)

        dp[0] = 1
        ans = 0
        for item in A:
            for j in range(m, -1, -1):
                if j - item < 0:
                    break
                if dp[j - item] == 1:
                    ans = max(ans, j)
                    dp[j] = 1
        return ans
