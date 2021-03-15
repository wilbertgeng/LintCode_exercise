"""443. Two Sum - Greater than target
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            if nums[left] + nums[right] >= target:
                ans += right - left
                right -= 1
            else:
                left += 1

        return ans 
