"""683. Word Break III
"""
class Solution:
    """
    @param s: A string
    @param dict: A set of word
    @return: the number of possible sentences.
    """
    def wordBreak3(self, s, dict):
        # Write your code here
        ## Practice:
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
        memo = {}
        s = s.lower()
        return self.dfs(0, s, lower_dict, memo)

    def dfs(self, idx, s, dict, memo):
        if idx == len(s):
            return 1
        res = 0
        for i in range(idx, len(s)):
            prefix = s[idx: i + 1]
            if prefix not in dict:
                continue
            res += self.dfs(i + 1, s, dict, memo)

        memo[s[idx:]] = res
        return res







        #####
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
        s = s.lower()
        return self.dfs(s, 0, lower_dict, {})

    def dfs(self, s, index, dict, memo):
        if index == len(s):
            return 1

        if s[index:] in memo:
            return memo[s[index:]]

        res = 0
        for i in range(index, len(s)):
            prefix = s[index :i + 1]
            if prefix not in dict:
                continue
            res += self.dfs(s, i + 1, dict, memo)

        memo[s[index:]] = res
        return res
