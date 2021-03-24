"""604. Window Sum
"""
class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        res = []
        if not nums or not k:
            return res
        n = len(nums)
        j = 0
        sum = 0
        for i in range(n):
            while j < n and j - i  < k:
                sum += nums[j]
                j += 1
            res.append(sum)
            sum -= nums[i]
            if j == n:
                break

        return res
