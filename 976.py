"""
976. 4Sum II
"""
class Solution:
    """
    @param A: a list
    @param B: a list
    @param C: a list
    @param D: a list
    @return: how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero
    """
    def fourSumCount(self, A, B, C, D):
        # Write your code here
        dict = {}
        for a in A:
            for b in B:
                dict[a + b] = dict.get(a + b, 0) + 1

        ans = 0
        for c in C:
            for d in D:
                ans += dict.get(- c - d, 0)

        return ans
