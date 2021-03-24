"""521. Remove Duplicate Numbers in Array
"""
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        # 1. do it in place. Otherwise: nums = list(set(nums))
        if len(nums) < 2:
            return len(nums)

        nums.sort()
        j = 1
        for i in range(len(nums)):
            while j < len(nums) and nums[j] == nums[i]:
                j += 1
            if j == len(nums):
                break ## !! be careful break first  
            nums[i + 1] = nums[j]

        return i + 1
