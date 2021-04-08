"""154. Regular Expression Matching"""
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        ### DP 错误答案！！
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for j in range(1, n + 1):
            if j >= 2:
                dp[0][j] = dp[0][j - 2] and p[j - 1] == "*"
            else:
                dp[0][j] = p[j - 1] == "*"

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = self.isMatch(s, p, i - 1, j - 2) and dp[i - 1][j - 2]
                else:
                    dp[i][j] = self.isMatch(s, p, i - 1, j - 1) and dp[i - 1][j - 1]

        return dp[m][n]

    def isMatch(self, s, p, x, y):
        return s[x] == p[y] or p[y] == "."






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
