"""10. String Permutation II"""
class Solution:
    """
    @param str: A string
    @return: all permutations
    """
    def stringPermutation2(self, str):
        # write your code here
        if not str:
            return [""]

        res = []
        str = list(str)
        str.sort()
        self.dfs(str, [], res)

        return res

    def dfs(self, s, path, res):
        if not s:
            path = "".join(path)
            res.append(path)
            return 

        for i in range(len(s)):
            if i > 0 and s[i] == s[i - 1]:
                continue
            path.append(s[i])
            self.dfs(s[:i] + s[i + 1:], path, res)
            path.pop()







        ####
        str = list(str)
        str.sort()
.
        visited = [False] * len(str)
        res = []
        self.dfs(str, [], visited, res)
        return res

    def dfs(self, string, path, visited, res):
        if len(path) == len(string):
            res.append("".join(path))
            return

        for i in range(len(string)):
            if visited[i]:
                continue
            if i > 0 and string[i] == string[i - 1] and not visited[i - 1]:
                continue

            visited[i] = True
            path += string[i]
            self.dfs(string, path, visited, res)
            path.pop()
            visited[i] = False
