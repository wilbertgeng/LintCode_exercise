"""
724. Minimum Partition
"""
class Solution:
    """
    @param nums: the given array
    @return: the minimum difference between their sums
    """
    def findMin(self, nums):
        # write your code here
        




        ###
        target = sum(nums) // 2
        n = len(nums)

        dp = [[False] * (target + 1) for _ in range(2)]
        dp[0][0] = True ## !!! Don't forget this!

        for i in range(1, n + 1):
            dp[i % 2][0] = True
            for j in range(target + 1):
                if nums[i - 1] > j:
                    dp[i % 2][j] = dp[(i - 1) % 2][j]
                else:
                    dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[(i - 1) % 2][j - nums[i - 1]]

        for j in range(target, -1, -1):
            if dp[n % 2][j] == True:
                return (sum(nums) - 2 * j) ## !!! Becareful what value needs to be returned

        return -1
