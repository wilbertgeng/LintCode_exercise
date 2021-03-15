"""
5. Kth Largest Element"""
class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or k < 1 or k > len(nums):
            return None
        return self.quickSelect(0, len(nums) - 1, len(nums) - k, nums)

    def quickSelect(self, start, end, k, nums):
        if start >= end:
            return nums[k]

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and pivot < nums[right]:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quickSelect(start, right, k, nums)
        if k >= left:
            return self.quickSelect(left, end, k, nums)

        return nums[k]










#####
