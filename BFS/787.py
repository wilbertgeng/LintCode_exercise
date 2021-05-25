"""787. The Maze"""
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        ## Practice:
        m = len(maze)
        n = len(maze[0])
        visited = set()
        queue = collections.deque([tuple(start)])

        while queue:
            i, j = queue.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x = i + dx
                y = j + dy
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if maze[x][y] == 0 and (x, y) not in visited:
                    if (x, y) == tuple(destination):
                        return True
                    visited.add((x, y))
                    queue.append((x, y))

        return False



        ####
        queue = collections.deque([(start[0], start[1])])
        visited = set()
        m = len(maze)
        n = len(maze[0])

        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            if i == destination[0] and j == destination[1]:
                return True
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i_new = i + x
                j_new = j + y
                while i_new >= 0 and i_new < m and j_new >= 0 and j_new < n and maze[i_new][j_new] != 1:
                    i_new += x
                    j_new += y
                i_new -= x
                j_new -= y
                if maze[i_new][j_new] == 0 and (i_new, j_new) not in visited:
                    queue.append((i_new, j_new))

        return False
