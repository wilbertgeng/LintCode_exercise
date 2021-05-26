"""562 · Backpack IV"""
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackIV(self, nums, target):
        # write your code here
        m = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(1, target + 1):
                if j < nums[i]:
                    continue
                dp[j] += dp[j - nums[i]]
        return dp[-1]
