"""610. Two Sum - Difference equals to target
"""
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (num1 < num2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        if not nums:
            return [-1, -1]

        target = abs(target)
        n = len(nums)
        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j] - nums[i] < target:
                j += 1
            if nums[j] - nums[i] == target:
                return [nums[i], nums[j]]

        return [-1, -1]
        ###
        ### no hash table
        if not nums:
            return [-1, -1]
        target = abs(target)
        n = len(nums)
        for i in range(n - 1):
            j = self.binarySearch(nums, i + 1, n - 1, target + nums[i])
            if j == -1:
                continue
            return [nums[i], nums[j]]

        return [-1, -1]

    def binarySearch(self, nums, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        return -1
