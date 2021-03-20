"""582. Word Break II
"""
class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """
    def wordBreak(self, s, wordDict):
        # write your code here
        return self.dfs(s, wordDict, {})

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        if not s:
            return []

        path = []
        for i in range(1, len(s)):
            prefix = s[:i]
            if prefix not in wordDict:
                continue

            suffix = s[i:]
            partitions = self.dfs(suffix, wordDict, memo)
            for partition in partitions:
                path.append(prefix + " " + partition)

        if s in wordDict:
            path.append(s)

        memo[s] = path
        return path
