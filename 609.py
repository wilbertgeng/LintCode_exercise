"""609. Two Sum - Less than or equal to target
"""
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        ### Practice:
        if not nums:
            return 0

        ans = 0
        left = 0
        right = len(nums) - 1
        nums.sort()
        while left < right:
            s = nums[left] + nums[right]
            if s <= target:
                ans += right - left
                left += 1
            else:
                right -= 1

        return ans


        ###
        if not nums:
            return 0

        n = len(nums)

        left = 0
        right = n - 1
        nums.sort()
        res = 0
        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res += right - left
                left += 1

        return res
