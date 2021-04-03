"""802 · Sudoku Solver"""
class Solution:
    """
    @param board: the sudoku puzzle
    @return: nothing
    """
    def solveSudoku(self, board):
        # write your code here
        used = self.createUsed(board)
        self.dfs(board, 0, used)

    def createUsed(self, board):
        used = {
            "row": [set() for _ in range(9)],
            "col": [set() for _ in range(9)],
            "box": [set() for _ in range(9)]
        }
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    continue
                used["row"][i].add(board[i][j])
                used["col"][j].add(board[i][j])
                used["box"][i //3 * 3 + j // 3].add(board[i][j])

        return used

    def dfs(self, board, index, used):
        if index == 81:
            return True

        i = index // 9
        j = index % 9

        if board[i][j] != 0:
            return self.dfs(board, index + 1, used)

        for val in range(1, 10):
            if not self.isValid(used, i, j, val):
                continue
            board[i][j] = val
            used["row"][i].add(val)
            used["col"][j].add(val)
            used["box"][i // 3 * 3 + j // 3].add(val)

            if self.dfs(board, index + 1, used):
                return True
            board[i][j] = 0
            used["row"][i].remove(val)
            used["col"][j].remove(val)
            used["box"][i // 3 * 3 + j // 3].remove(val)

        return False

    def isValid(self, used, i, j, val):
        if val in used["row"][i] or val in used["col"][j] or val in used["box"][i // 3 * 3 + j // 3]:
            return False

        return True
