"""152 · Combinations"""
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if not n or not k:
            return [[]]

        res = []
        self.dfs(0, n, k, [], res)
        return res

    def dfs(self, start, n, k, path, res):
        if k == 0:
            res.append(list(path))
            return
        if start == n:
            return
        for i in range(start, n):
            num = i + 1
            path.append(num)
            self.dfs(i + 1, n, k - 1, path, res)
            path.pop()
