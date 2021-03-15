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
