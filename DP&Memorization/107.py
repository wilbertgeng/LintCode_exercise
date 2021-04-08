"""
107. Word Break"""
class Solution:
    """
    @param s: A string
    @param wordSet: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, wordSet):
        # write your code here


        ### O(n^2)
        if not s:
            return True

        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if s[j: i] not in wordSet:
                    continue
                if dp[j] = True:
                    dp[i] = True
                    break


        return dp[n]





        ##### O(n*l + m)
        n = len(s)

        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for length in range(1, i + 1):
                if not dp[i - length]:
                    continue
                if s[i - length: i] in wordSet:
                    dp[i] = True
                    break

        return dp[-1]
