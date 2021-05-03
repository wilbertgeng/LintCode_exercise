"""192. Wildcard Matching
"""
class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        ### Practice: DP
        m = len(s)
        n = len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1] or dp[i - 1][j - 1]

        return dp[-1][-1]



        ## Practce DFS Memorization
        return self.isMatchHelper(0, s, 0, p, {})

    def isMatchHelper(self, s_idx, s, p_idx, p, memo):
        if (s_idx, p_idx) in memo:
            return memo[(s_idx, p_idx)]
        if p_idx == len(p):
            return s_idx == len(s)
        if s_idx == len(s):
            return self.isAllStatrs(p_idx, p)

        s_char = s[s_idx]
        p_char = p[p_idx]

        if p_char != "*":
            match = self.isCharMatch(s_char, p_char) and self.isMatchHelper(s_idx + 1, s, p_idx + 1, p, memo)
        else:
            match = self.isMatchHelper(s_idx + 1, s, p_idx, p, memo) or self.isMatchHelper(s_idx, s, p_idx + 1, p, memo)

        memo[(s_idx, p_idx)] = match

        return match

    def isCharMatch(self, char_s, char_p):
        return char_s == char_p or char_p == "?"

    def isAllStatrs(self, p_idx, p):
        while p_idx < len(p):
            if p[p_idx] != "*":
                return False
            p_idx += 1

        return True



        ### DP
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and p[j - 1] == "*"

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == "?")

        return dp[m][n]



        ##### DFS Memorization

        return self.isMatchHelper(s, 0, p, 0, {})

    def isMatchHelper(self, s, s_index, p, p_index, memo):
        if (s_index, p_index) in memo:
            return memo[(s_index, p_index)]
        if p_index == len(p):
            return s_index == len(s)

        if s_index == len(s):
            return self.isAllStatrs(p, p_index)

        s_char = s[s_index]
        p_char = p[p_index]

        if p_char != "*":
            match = self.isCharMatch(s_char, p_char) and self.isMatchHelper(s, s_index + 1, p, p_index + 1, memo)
        else:
            match = self.isMatchHelper(s, s_index, p, p_index + 1, memo) or self.isMatchHelper(s, s_index + 1, p, p_index, memo)

        memo[(s_index, p_index)] = match

        return match

    def isAllStatrs(self, p, p_index):
        for i in range(p_index, len(p)):
            if p[i] != "*":
                return False

        return True

    def isCharMatch(self, s_char, p_char):
        return s_char == p_char or p_char == "?"
