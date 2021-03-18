"""
563. Backpack V
"""
class Solution:
    """
    @param nums: an integer array and all positive numbers
    @param target: An integer
    @return: An integer
    """
    def backPackV(self, nums, target):
        # write your code here
        m = len(nums)

        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, m + 1):
            for j in range(target, -1, -1):
                if nums[i - 1] <= j:
                    dp[j] += dp[j - nums[i - 1]]

        print(dp)

        return dp[-1]
