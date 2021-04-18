"""460. Find K Closest Elements
LeetCode 658
"""
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        ## Practice:
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        return self.findKClosest(k, start, nums, target)

    def findKClosest(self, k, idx, nums, target):
        res = []
        l = idx
        r = idx + 1
        for _ in range(k):
            if self.leftCloser(l, r, nums, target):
                res.append(nums[l])
                l -= 1
            else:
                res.append(nums[r])
                r += 1
        return res

    def leftCloser(self, l, r, nums, target):
        if r >= len(nums):
            return True
        if l < 0:
            return False

        return abs(nums[l] - target) <= abs(nums[r] - target)










        ####
        res = []
        right = self.findClosest(A, target)
        left = right - 1

        for _ in range(k):
            if self.isLeftCloser(A, left, right, target):
                res.append(A[left])
                left -= 1
            else:
                res.append(A[right])
                right += 1

        return res

    def findClosest(self, A, target):
        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] >= target:
            return start
        if A[end] >= target:
            return end

        return len(A)

    def isLeftCloser(self, A, left, right, target):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
