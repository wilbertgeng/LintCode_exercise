"""603. Largest Divisible Subset
"""
class Solution:
    """
    @param nums: a set of distinct positive integers
    @return: the largest subset
    """
    def largestDivisibleSubset(self, nums):
        # write your code here
        if not nums:
            return 0

        nums.sort()
        prev = {}
        dp = {}
        for num in nums:
            dp[num] = 1
            prev[num] = -1

        largest = 0
        last_num = nums[0]
        for num in nums:
            for factor in self.getFactors(num):
                if factor not in dp:
                    continue
                if dp[factor] + 1 > dp[num]:
                    dp[num] = dp[factor] + 1
                    prev[num] = factor
                    if dp[num] > dp[last_num]:
                        last_num = num

        return self.findPath(last_num, prev)

    def getFactors(self, num):
        if num == 1:
            return []
        factor = 1
        factors = []
        while factor * factor <= num:
            if num % factor == 0:
                factors.append(factor)
                if factor * factor != num and factor != 1:
                    factors.append(num // factor)
            factor += 1

        return factors

    def findPath(self, num, prev):
        path = []
        while num != -1: ## be careful! not prev[num]
            path.append(num)
            num = prev[num]

        return path[::-1]






##
