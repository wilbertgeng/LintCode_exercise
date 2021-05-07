"""76. Longest Increasing Subsequence"""
class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        ### Practice:
        if not nums:
            return 0
        n = len(nums)
        rank = [float('inf')] * (n + 1)
        rank[0] = float('-inf')

        longest = 0
        for num in nums:
            index = self.gte(rank, num)
            rank[index] = num
            longest = max(longest, index)
        return longest

    def gte(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        return end

        ### DP: O(n^2)
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue
                dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


        ### Binary Search O(nlogn)
        n = len(nums)
        lis = [float('inf')] * (n + 1)
        lis[0] = float('-inf')

        longest = 0
        for num in nums:
            index = self.BiSearch_gte(lis, num)
            lis[index] = num
            longest = max(longest, index)

        return longest

    def BiSearch_gte(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        return end

        ### Practice
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)






##
