"""34 · N-Queens II"""
class Solution:
    """
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    def totalNQueens(self, n):
        # write your code here
        self.res = 0
        self.search(n, [])
        return self.res

    def search(self, n, cols):
        row = len(cols)
        if row == n:
            self.res += 1
            return

        for col in range(n):
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols)
            cols.pop()

    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True

    
