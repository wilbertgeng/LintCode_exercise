"""630. Knight Shortest Path II
"""
DIRECTIONS = [(-1, -2), (1, -2), (-2, -1), (2, -1)]
class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    def shortestPath2(self, grid):
        # write your code here
        m = len(grid)
        n = len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

        if grid[0][0] == 1:
            return -1
        dp[0][0] = 0
        for j in range(n): # loop Y first then X
            for i in range(m):
                if grid[i][j] == 1:
                    continue
                for x, y in DIRECTIONS:
                    x_prev = i + x
                    y_prev = j + y
                    if 0 <= x_prev < m and 0 <= y_prev < n:
                        dp[i][j] = min(dp[i][j], dp[x_prev][y_prev] + 1)
        print(dp)
        if dp[-1][-1] == float('inf'):
            return -1

        return dp[-1][-1]




####
