"""1870. Number of Substrings with All Zeroes
"""
class Solution:
    """
    @param str: the string
    @return: the number of substrings
    """
    def stringCount(self, str):
        # Write your code here.
        if not str:
            return 0
        j = 1
        n = len(str)
        ans = 0
        for i in range(n):
            j = max(j, i + 1)
            if str[i] != "0":
                continue
            while j < n and str[j] == "0":
                j += 1
            ans += j - i

        return ans
