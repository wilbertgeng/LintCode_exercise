"""622 · Frog Jump"""
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        # write your code here


        # wrong answer
        if not stones:
            return False

        n = len(stones)
        dp = [False] * n
        dp[0] = True
        last_step = 0
        for i in range(1, n):
            if stones[i] - stones[i - 1] > last_step + 1 or stones[i] - stones[i - 1] < last_step - 1:
                dp[i] = False
                break
            else:
                dp[i] = dp[i - 1]

            last_step = stones[i] - stones[i - 1]

        return dp[-1]
