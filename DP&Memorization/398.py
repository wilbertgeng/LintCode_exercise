"""398. Longest Continuous Increasing Subsequence II
"""
class Solution:
    """
    @param matrix: A 2D-array of integers
    @return: an integer
    """
    def longestContinuousIncreasingSubsequence2(self, matrix):
        # write your code here
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        points = []
        for i in range(m):
            for j in range(n):
                points.append((matrix[i][j], i, j))

        points.sort()
        path = {}
        for i in range(len(points)):
            key = (points[i][1], points[i][2])
            path[key] = 1
            for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                x = points[i][1] + a
                y = points[i][2] + b
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if matrix[x][y] < points[i][0]:
                    path[key] = max(path[key], path[(x, y)] + 1)

        return max(path.values())
