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
