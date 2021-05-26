"""669 · Coin Change"""
class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here
        m = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(m):
            for j in range(1, amount + 1):
                if j < coins[i]:
                    continue
                dp[j] = min(dp[j - coins[i]] + 1, dp[j])
        return dp[-1] if dp[-1] != float('inf') else -1
