"""61. Search for a Range"""
class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        # write your code here
        if not A:
            return [-1, -1]
        res = []
        start = 0
        end = len(A) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid

        if A[start] == target:
            res.append(start)
            end = start
        elif A[end] == target:
            res.append(end)
        else:
            return [-1, -1]
            
        occur = end
        for i in range(end, len(A)):
            if A[i] != target:
                break
            else:
                occur = i
        res.append(occur)

        return res
