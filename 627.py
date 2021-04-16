"""627. Longest Palindrome
"""
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        ### Practice:
        d = {}

        for l in s:
            d[l] = d.get(l, 0) + 1
        length = 0
        for l in d:
            if d[l] % 2 == 0:
                length += d[l]
            else:
                length += d[l] - 1

        return length + 1 if length != len(s) else length




        ######
        if not s:
            return 0
        d = {}
        for l in s:
            if l in d:
                d[l] += 1
            else:
                d[l] = 1

        res = 0
        for cnt in d.values():
            res += cnt//2*2

        return res if res == len(s) else res + 1
