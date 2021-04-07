"""154. Regular Expression Matching"""
class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        ### DP
        






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
