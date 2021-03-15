"""159. Find Minimum in Rotated Sorted Array"""

class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= nums[end]:
                end = mid
            else:
                start = mid

        return min(nums[start], nums[end])
