"""533 · Two Sum - Closest to target"""
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        nums.sort()
        l = 0
        r = len(nums) - 1

        res = float('inf')
        while l < r:
            s = nums[l] + nums[r]
            res = min(res, abs(s - target))
            if s < target:
                l += 1
            elif s > target:
                r -= 1
            else:
                return 0

        return res
