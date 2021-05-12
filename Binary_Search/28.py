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
        ## Practice:
        m = len(matrix)
        n = len(matrix[0])

        col_first = []
        for i in range(m):
            col_first.append(matrix[i][0])

        row_index = self.binarySearch(col_first, target)
        col_index = self.binarySearch(matrix[row_index], target)
        return matrix[row_index][col_index] == target

    def binarySearch(self, nums, target):
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] <= target:
            return end
        return start




        ## 超时了
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
