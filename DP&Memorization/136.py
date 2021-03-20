"""136. Palindrome Partitioning
"""
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        return self.dfs(s, {})

    def dfs(self, s, memo):
        if not s:
            return []

        if s in memo:
            return memo[s]

        path = []
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix != prefix[::-1]:
                continue
            suffix = s[i:]
            partitions = self.dfs(suffix, memo)
            for partition in partitions:
                path.append([prefix] + partition)

        if s == s[::-1]:
            path.append([s])

        memo[s] = path
        return path
