"""154. Regular Expression Matching"""
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        ### Practice:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1] or dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == ".")

        return dp[-1][-1]





        ### DP practice:
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == ".":
                        dp[i][j] = dp[i - 1][j] or dp[i][j]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == ".":
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[-1][-1]



        ## DFS memorization practice:
        return self.dfs(s, 0, p, 0, {})

    def dfs(self, s, s_idx, p, p_idx, memo):
        if (s_idx, p_idx) in memo:
            return memo[(s_idx, p_idx)]

        if s_idx == len(s):
            return self.isEmpty(p[p_idx:])

        if p_idx == len(p):
            return False

        if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
            match = self.isCharMatch(s, s_idx, p, p_idx) and self.dfs(s, s_idx + 1, p, p_idx, memo) or self.dfs(s, s_idx, p, p_idx + 2, memo)
        else:
            match = self.isCharMatch(s, s_idx, p, p_idx) and self.dfs(s, s_idx + 1, p, p_idx + 1, memo)

        memo[(s_idx, p_idx)] = match

        return match

    def isCharMatch(self, s, s_idx, p, p_idx):
        return s[s_idx] == p[p_idx] or p[p_idx] == "."

    def isEmpty(self, p):
        if len(p) % 2 == 1:
            return False

        for i in range(len(p) // 2):
            if p[i * 2 + 1] != "*":
                return False
        return True







        ### DFS Memorization
        return self.isMatchHelper(s, 0, p, 0, {})

    def isMatchHelper(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(s) == i:
            return self.isEmpty(p[j:])

        if len(p) == j:
            return False

        if j + 1 < len(p) and p[j + 1] == "*":
            match = self.isCharMatch(s, i, p, j) and self.isMatchHelper(s, i + 1, p, j, memo) or self.isMatchHelper(s, i, p, j + 2, memo)
        else:
            match = self.isCharMatch(s, i, p, j) and self.isMatchHelper(s, i + 1, p, j + 1, memo)

        memo[(i, j)] = match

        return match

    def isCharMatch(self, s, i, p, j):
        return s[i] == p[j] or p[j] == "."

    def isEmpty(self, p):
        if len(p) % 2 == 1:
            return False

        for i in range(len(p) // 2):
            if p[i * 2 + 1] != "*":
                return False

        return True
