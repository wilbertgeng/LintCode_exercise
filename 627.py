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
        if not s:
            return 0
        d = {}

        for l in s:
            d[l] = d.get(l, 0) + 1

        ans = 0
        for value in d.values():
            ans += value // 2 * 2

        return ans if ans == len(s) else ans + 1





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
