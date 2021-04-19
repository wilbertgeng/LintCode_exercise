"""611. Knight Shortest Path
"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        ## Practice:
        if not grid or grid[source.x][source.y] == 1:
            return -1
        if source.x == destination.x and source.y == destination.y:
            return 0

        self.directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1)]
        queue = collections.deque([(source.x, source.y)])
        steps = {(source.x, source.y): 0}


        while queue:
            i, j = queue.popleft()
            if i == destination.x and j == destination.y:
                return steps[(i, j)]
            for dx, dy in self.directions:
                x = i + dx
                y = j + dy
                if not self.isValid(x, y, grid, steps):
                    continue
                steps[(x, y)] = steps[(i, j)] + 1
                queue.append((x, y))

        return -1

    def isValid(self, i, j, grid, steps):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1 or (i, j) in steps:
            return False

        return True




        ####
        if not grid or grid[destination.x][destination.y] == 1:
            return -1
        if source.x == destination.x and source.y == destination.y:
            return 0

        self.directions = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

        queue = collections.deque([(source.x, source.y)])
        steps = {(source.x, source.y): 0}

        while queue:
            x, y = queue.popleft()
            for i, j in self.directions:
                newX = x + i
                newY = y + j
                if newX == destination.x and newY == destination.y:
                    return steps[(x, y)] + 1
                if not self.isValid(newX, newY, grid, steps):
                    continue
                queue.append((newX, newY))
                steps[(newX, newY)] = steps[(x, y)] + 1
                ###
                if self.isValid(newX, newY, grid, steps):
                    queue.append((newX, newY))
                    steps[(newX, newY)] = steps[(x, y)] + 1

        return -1

    def isValid(self, i, j, grid, steps):
        m = len(grid)
        n = len(grid[0])
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1 or (i, j) in steps:
            return False
        return True












###
