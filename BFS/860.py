"""860 · Number of Distinct Islands"""
class Solution:
    """
    @param grid: a list of lists of integers
    @return: return an integer, denote the number of distinct islands
    """
    def numberofDistinctIslands(self, grid):
        # write your code here
        if not grid:
            return 0

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        visited = set()
        res = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    res.add(self.bfs(i, j, grid, visited))

        return len(res)

    def bfs(self, i, j, grid, visited):
        queue = collections.deque([(i, j)])
        ans = "1"
        while queue:
            i, j = queue.popleft()
            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if not self.isValid(x, y, grid, visited):
                    ans += "0"
                    continue
                ans += "1"
                queue.append((x, y))
                visited.add((x, y))

        return ans

    def isValid(self, i, j, grid, visited):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 0 or (i, j) in visited:
            return False
        return True












#####
