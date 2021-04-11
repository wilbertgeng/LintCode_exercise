"""680 · Split String"""
class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        # write your code here
        if not s:
            return [[]]

        res = []

        self.dfs(s, 0, [], res)
        return res

    def dfs(self, s, index, path, res):
        if index == len(s):
            res.append(list(path))
            return

        path.append(s[index])
        self.dfs(s, index + 1, path, res)
        path.pop()

        if index + 2 <= len(s):
            path.append(s[index:index + 2])
            self.dfs(s, index + 2, path, res)
            path.pop()
