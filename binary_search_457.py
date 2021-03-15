"""457. Classical Binary Search
"""

class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        ###
        """当你发现有一个问题，用O(N)的时间复杂度非常好做，
        或者面试官说：“你给我优化一下这个算法。”那么你优化的思路就是优化到O(logn)，
        也就是尝试使用二分去做，这就是二分算法的判断条件"""

        ### Template: same as find 1st position
        ## review 585
        if not nums:
            return -1
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            if nums[mid] < target:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1

        ### Last Position 458
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return -1

        ### First Position 14
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1









        ## recursion
        return self.binarySearch(0, len(nums) - 1, nums, target)

    def binarySearch(self, left, right, nums, target):
        if left > right:
            return -1

        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binarySearch(mid + 1, right, nums, target)
        else:
            return self.binarySearch(left, mid - 1, nums, target)
