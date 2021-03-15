"""75. Find Peak Element
"""
class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        if not A:
            return None

        start = 1
        end = len(A) - 2

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[mid - 1]:
                end = mid
            elif A[mid] < A[mid + 1]: ## !! use elif not just if 
                start = mid
            else:
                return mid

        if A[start] < A[end]:
            return end

        return start
