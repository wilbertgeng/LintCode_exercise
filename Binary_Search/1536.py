"""1536. Find First and Last Position of Element in Sorted Array"""
class Solution:
    """
    @param nums: the array of integers
    @param target:
    @return: the starting and ending position
    """
    def searchRange(self, nums, target):
        # Write your code here.
        res = []
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            res.append(start)
            end = start
        elif nums[end] == target:
            res.append(end)
        else:
            return [-1, -1]
        for i in range(end, len(nums)):
            if nums[i] != target:
                res.append(i - 1)
                break 

        return res
