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
