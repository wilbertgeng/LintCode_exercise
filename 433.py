"""433. Number of Islands"""
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        ## BFS
        if not grid:
            return 0
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m = len(grid)
        n = len(grid[0])
        islands = 0

        visited = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    self.bfs(i, j, grid, visited)
                    islands += 1

        return islands

    def bfs(self, i, j, grid, visited):
        queue = collections.deque([(i, j)])
        visited.add((i, j))
        while queue:
            x, y = queue.popleft()
            for x1, y1 in self.directions:
                newX, newY = x + x1, y + y1
                if self.isValid(newX, newY, grid, visited):
                    visited.add((newX, newY))
                    queue.append((newX, newY))


    def isValid(self, i, j, grid, visited):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0:
            return False
        return True














########
