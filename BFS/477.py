"""477 · Surrounded Regions"""
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        # write your code here
        if not board:
            return None
        m = len(board)
        n = len(board[0])

        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        for i in (0, m - 1):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    self.dfsBound(i, j, board, visited)

        for j in (0, n - 1):
            for i in range(m):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    self.dfsBound(i, j, board, visited)
        for i in range(1, m):
            for j in range(1, n):
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    self.dfs(i, j, board, visited)
        for i in range(m):
            for j in range(n):
                if board[i][j] == ".":
                    board[i][j] = "O"
                if board[i][j] == "*":
                    board[i][j] = "X"


    def dfs(self, i, j, board, visited):
        board[i][j] = "*"
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            if not self.isValid(x, y, board, visited):
                continue
            visited.add((x, y))
            self.dfs(x, y, board, visited)


    def dfsBound(self, i, j, board, visited):
        board[i][j] = "."
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            if not self.isValid(x, y, board, visited):
                continue
            visited.add((x, y))
            self.dfsBound(x, y, board, visited)

    def isValid(self, i, j, board, visited):
        m = len(board)
        n = len(board[0])
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] == "X" or (i, j) in visited:
            return False
        return True
















#####
