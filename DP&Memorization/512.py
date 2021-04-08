"""512 · Decode Ways"""
class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0

        dp = [1, 0, 0]
        dp[1] = self.decodeOK(s[0])

        for i in range(2, n + 1):
            dp[i % 3] = dp[(i - 1) % 3] * self.decodeOK(s[i - 1: i]) +\
                        dp[(i - 2) % 3] * self.decodeOK(s[i - 2: i])

        return dp[n % 3]

    def decodeOK(self, string):
        code = int(string)
        l = len(string)
        if l == 1 and 1 <= code < 10:
            return 1
        if l == 2 and 10 <= code <= 26:
            return 1
        return 0
