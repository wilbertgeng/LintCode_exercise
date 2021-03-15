"""6. Merge Two Sorted Arrays
"""

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        i = 0
        j = 0
        res = []
        n = len(A) - 1
        m = len(B) - 1

        while i <= n and j <= m:
            if A[i] < B[j]:
                res.append(A[i])
                i += 1
            else:
                res.append(B[j])
                j += 1

        if i == n + 1:
            res += B[j:]
        else:
            res += A[i:]

        return res
