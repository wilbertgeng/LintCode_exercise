"""462. Total Occurrence of Target
"""
class Solution:
    """
    @param A: A an integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def totalOccurrence(self, A, target):
        # write your code here
        ### Practice:
        if not A:
            return 0
        index = self.binarySearch(A, target)

        if index == None:
            return 0
        cnt = 0
        for i in range(index, len(A)):
            if A[i] == target:
                cnt += 1
        return cnt

    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1

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
        return None






        ######
        if not A:
            return 0
        start = 0
        end = len(A) - 1
        count = 0

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        occur = 0
        if A[start] == target:
            occur = start
        elif A[end] == target:
            occur = end
        else:
            return 0

        for i in range(occur, len(A)):
            if A[i] != target:
                break
            count += 1

        return count
