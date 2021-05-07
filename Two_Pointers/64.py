"""64. Merge Sorted Array (easy version)
"""
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        pt1 = m - 1
        pt2 = n - 1
        pt = m + n - 1
        while pt1 != -1 and pt2 != -1:
            if A[pt1] >= B[pt2]:
                A[pt] = A[pt1]
                pt1 -= 1
            else:
                A[pt] = B[pt2]
                pt2 -= 1
            pt -= 1

        if pt2 >= 0:
            A[:pt2 + 1] = B[:pt2 + 1]





        ###

        while m > 0 and n > 0:
            if A[m - 1] >= B[n - 1]:
                A[m + n - 1] = A[m - 1]
                m -= 1
            else:
                A[m + n - 1] = B[n - 1]
                n -= 1

        if n > 0:
            A[:n] = B[:n]
