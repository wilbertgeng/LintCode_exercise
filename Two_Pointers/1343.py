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
        ## Practice:
        if not A and not B:
            return ""
        if not A or not B:
            return A or B
        m = len(A)
        n = len(B)

        pt1 = m - 1
        pt2 = n - 1

        stack = []
        while pt1 != -1 and pt2 != -1:
            num = int(A[pt1]) + int(B[pt2])
            stack.append(str(num))
            pt1 -= 1
            pt2 -= 1
        while pt1 != -1:
            stack.append(A[pt1])
            pt1 -= 1
        while pt2 != -1:
            stack.append(B[pt2])
            pt2 -= 1

        res = ""
        while stack:
            res += stack.pop()
        return res



        ####
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
