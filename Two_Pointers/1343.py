"""1343. Sum of Two Strings
"""
class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        ptA = len(A) - 1
        ptB = len(B) - 1

        res = ""
        while ptA >= 0 and ptB >= 0:
            path = str(int(A[ptA]) + int(B[ptB]))
            res = path + res
            ptA -= 1
            ptB -= 1

        if ptA >= 0:
            res = A[:ptA + 1] + res
        else:
            res = B[:ptB + 1] + res

        return res
