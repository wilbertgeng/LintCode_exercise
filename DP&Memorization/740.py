"""740 · Coin Change 2"""
class Solution:
    """
    @param amount: a total amount of money amount
    @param coins: the denomination of each coin
    @return: the number of combinations that make up the amount
    """
    def change(self, amount, coins):
        # write your code here
        m = len(coins)

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(1, amount + 1):
                if j < coins[i]:
                    continue
                dp[j] += dp[j - coins[i]]
        return dp[-1]
