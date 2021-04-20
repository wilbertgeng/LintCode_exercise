"""598 · Zombie in Matrix"""
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        # write your code here
        if not grid:
            return -1

        m = len(grid)
        n = len(grid[0])
        queue = collections.deque([])
        visited = set()

        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited.add((i, j))
                    cnt += 1
                if grid[i][j] == 0:
                    cnt += 1

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        days = -1
        while queue:
            days += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for dx, dy in self.directions:
                    x = i + dx
                    y = j + dy
                    if not self.isValid(x, y, grid, visited):
                        continue
                    queue.append((x, y))
                    visited.add((x, y))
        if cnt == len(visited):
            return days
        return -1

    def isValid(self, i, j, grid, visited):
        m = len(grid)
        n = len(grid[0])

        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 2 or (i, j) in visited:
            return False
        return True















######
