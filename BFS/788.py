"""788. The Maze II
"""
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        m = len(maze)
        n = len(maze[0])
        queue = collections.deque([tuple(start)])
        steps = {tuple(start): 0}

        while queue:
            i, j = queue.popleft()

            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                i_new = i + x
                j_new = j + y
                while 0 <= i_new < m and 0 <= j_new < n and maze[i_new][j_new] != 1:
                    i_new += x
                    j_new += y
                i_new -= x
                j_new -= y
                if maze[i_new][j_new] == 0:
                    if (i_new, j_new) not in steps:
                        steps[(i_new, j_new)] = steps[(i, j)] + abs(i_new - i + j_new - j)
                        queue.append((i_new, j_new))
                    if steps[(i_new, j_new)] > steps[(i, j)] + abs(i_new - i + j_new - j): #如果发现了最短路径 需要写入queue重新计算
                        steps[(i_new, j_new)] = steps[(i, j)] + abs(i_new - i + j_new - j)
                        queue.append((i_new, j_new))
        if tuple(destination) in steps:
            return steps[tuple(destination)]
        return -1
