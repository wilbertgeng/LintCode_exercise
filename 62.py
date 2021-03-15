"""62. Search in Rotated Sorted Array
"""
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        ### binary search twice
        def search(self, A, target):
        # write your code here
        if not A:
            return -1

        index = self.findMin(A, 0, len(A) - 1)
        if A[index] <= target <= A[-1]:
            return self.binarySearch(A, index, len(A) - 1, target)
        return self.binarySearch(A, 0, index - 1, target)

    def binarySearch(self, A, start, end, target):
        if end < 0:
            end = len(A) - 1 ## !! in case A is a sorted array
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1     ## !! in case target not in A

    def findMin(self, A, start, end):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid

        if A[start] < A[end]:
            return start
        else:
            return end


        ### binary search once
        if not A:
            return -1

        start = 0
        end = len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        return -1









#####
