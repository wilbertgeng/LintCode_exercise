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
        ### Practice:
        return self.dfs(0, s, wordDict, {})

    def dfs(self, idx, s, dict, memo):
        if idx == len(s):
            return []
        if s[idx:] in memo:
            return memo[s[idx:]]
        res = []
        path = ""
        for i in range(idx, len(s)):
            prefix = s[idx: i + 1]
            if prefix not in dict:
                continue
            path = prefix
            for sentence in self.dfs(i + 1, s, dict, memo):
                res.append(path + " " + sentence)
        if s[idx:] in dict:
            res.append(s[idx:]) ## !!

        memo[s[idx:]] = res 

        return res











        ##
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
