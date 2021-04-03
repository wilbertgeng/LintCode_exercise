"""33 · N-Queens"""
class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    def solveNQueens(self, n):
        # write your code here
        res = []
        self.search(n, [], res)
        return res

    def search(self, n, cols, res):
        row = len(cols)
        if row == n:
            res.append(self.draw(cols))
            return

        for col in range(n):
            if not self.isValid(cols, row, col):
                continue
            cols.append(col)
            self.search(n, cols, res)
            cols.pop()

    def isValid(self, cols, row, col):
        for r, c in enumerate(cols):
            if c == col:
                return False
            if r + c == row + col or r - c == row - col:
                return False
        return True

    def draw(self, cols):
        ans = []
        for i in range(len(cols)):
            ans.append("".join(["Q" if j == cols[i] else "." for j in range(len(cols))]))

        return ans
