"""397 · Longest Continuous Increasing Subsequence"""
class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        # write your code here
        if not A:
            return 0

        n = len(A)

        longest = 1
        increase = 1
        decrease = 1

        for i in range(1, n):
            if A[i] > A[i - 1]:
                increase += 1
                decrease = 1
            if A[i] < A[i - 1]:
                decrease += 1
                increase = 1
            longest = max(longest, increase, decrease)

        return longest
