"""608 · Two Sum II - Input array is sorted"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        l = 0
        r = len(nums) - 1

        res = []
        while l < r:
            while l < r and nums[l] + nums[r] < target:
                l += 1
            while l < r and nums[l] + nums[r] > target:
                r -= 1
            if l < r and nums[l] + nums[r] == target:
                res.append(l + 1)
                res.append(r + 1)
                l += 1
                r -= 1

        return res
