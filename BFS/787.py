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
