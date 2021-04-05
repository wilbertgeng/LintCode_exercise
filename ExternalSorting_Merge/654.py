"""654 · Sparse Matrix Multiplication"""
class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        if not A or not B:
            return []

        m = len(A)
        n = len(A[0])
        l = len(B[0])

        res = [[0] * l for _ in range(m)]

        for i in range(m):
            for j in range(n):
              if A[i][j] == 0:
                continue
              for k in range(l):
                  res[i][k] += A[i][j] * B[j][k]

        return res 
