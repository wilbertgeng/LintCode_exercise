"""28. Search a 2D Matrix
"""
class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        m = len(matrix)
        n = len(matrix[0])

        i = m - 1
        j = 0

        while i >= 0 and j < n:
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1

            else:
                return True

        return False 
