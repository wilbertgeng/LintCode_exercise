"""132. Word Search II
"""
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        # write your code here
        self.directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])

        dict = set(words)
        res = set()
        length = 0
        prefix = set()
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])
        for word in words:
            length = max(length, len(word))
        for i in range(m):
            for j in range(n):
                visited = set()
                visited.add((i, j))
                self.dfs(i, j, board, visited, dict, board[i][j], res, length, prefix)
        return list(res)

    def dfs(self, i, j, board, visited, dict, path, res, length, prefix):
        if len(path) > length or path not in prefix:
            return

        if path in dict:
            res.add(path)
        for dx, dy in self.directions:
            x = i + dx
            y = j + dy
            if not self.isValid(x, y, board, visited):
                continue
            visited.add((x, y))
            self.dfs(x, y, board, visited, dict, path + board[x][y], res, length, prefix)
            visited.remove((x, y))

    def isValid(self, x, y, board, visited):
        m = len(board)
        n = len(board[0])
        if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited:
            return False
        return True 






        ####
        prefix = set()
        for word in words:
            for i in range(len(word)):
                if word[:i + 1] not in prefix:
                    prefix.add(word[:i + 1])

        visited = set()
        result = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in prefix:
                    char = board[i][j]
                    self.dfs(i, j, board, char, set([(i, j)]), result, words, prefix)
        return list(result)

    def dfs(self, x, y, board, char, visited, result, words, prefix):
        if char not in prefix:
            return
        if char in words:
            result.add(char)

        for a, b in DIRECTIONS:
            newX = x + a
            newY = y + b

            if not self.isValid(newX, newY, board):
                continue
            if (newX, newY) in visited:
                continue

            visited.add((newX, newY))
            self.dfs(newX, newY, board, char + board[newX][newY], visited, result, words, prefix)
            visited.remove((newX, newY))

    def isValid(self, x, y, board):
        if 0 <= x < len(board) and 0 <= y < len(board[0]):
            return True
        return False
