"""794 · Sliding Puzzle II"""
class Solution:
    """
    @param init_state: the initial state of chessboard
    @param final_state: the final state of chessboard
    @return: return an integer, denote the number of minimum moving
    """
    def minMoveStep(self, init_state, final_state):
        # # write your code here
        start = self.matrixToString(init_state)
        end = self.matrixToString(final_state)

        queue = collections.deque([(start, 0)])
        visited = set()
        visited.add(start)

        while queue:
            status_curr, step_curr = queue.popleft()
            if status_curr == end:
                return step_curr
            for status in self.findNext(status_curr):
                if status in visited:
                    continue
                visited.add(status)
                queue.append((status, step_curr + 1))

        return -1



    def findNext(self, state):
        states = []
        index_zero = state.find("0")
        x, y = index_zero // 3, index_zero % 3

        for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x_n, y_n = x + dir[0], y + dir[1]
            if 0 <= x_n < 3 and 0 <= y_n < 3:
                state_new = list(state)
                state_new[index_zero], state_new[x_n * 3 + y_n] = state_new[x_n * 3 + y_n], state_new[index_zero]
                state_new = "".join(state_new)
                states.append(state_new)

        return states    

    def matrixToString(self, state):
        m = len(state)
        n = len(state[0])
        state_string = []

        for i in range(m):
            state_string += state[i]

        return "".join(str(item) for item in state_string)
