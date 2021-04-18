"""31. Partition Array
"""
class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if not nums:
            return 0

        l = 0
        r = len(nums) - 1
        if l == r:
            return r
        while l <= r:
            while l <= r and nums[l] < k:
                l += 1
            while l <= r and nums[r] >= k:
                r -= 1
            if l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        return l







        ###
        if not nums:
            return 0
        return self.partition(0, len(nums) - 1, nums, k)
    def partition(self, left, right, nums, k):
        if left >= right:
            return left

        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left
