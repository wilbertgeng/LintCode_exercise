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
