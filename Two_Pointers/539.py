"""539. Move Zeroes"""
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        ## Practice:
        l = 0
        r = 0
        n = len(nums)

        while r < n:
            if r < n and nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        while l < n:
            if nums[l] != 0:
                nums[l] = 0
            l += 1



        #####
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

        while left < len(nums):
            if nums[left] != 0:
                nums[left] = 0
            left += 1
