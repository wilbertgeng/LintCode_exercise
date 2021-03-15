"""
1179. Friend Circles
"""
class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        # Write your code here
        if not M:
            return 0
        visited = set()
        cnt = 0
        for x in range(len(M)):
            if x not in visited:
                visited.add(x)
                self.bfs(x, M, visited)
                cnt += 1

        return cnt

    def bfs(self, x, M, visited):
        queue = [x]
        while queue:
            q = queue.pop(0)
            for j in range(len(M)):
                if M[q][j] == 1 and j not in visited:
                    visited.add(j)
                    queue.append(j)
