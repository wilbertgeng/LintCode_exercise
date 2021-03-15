"""200. Longest Palindromic Substring
"""

class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here

        ### Practice
        if not s:
            return s

        ans = (1, 0)
        for i in range(len(s)):
            ans = max(ans, self.isPalindrome(s, i, i))
            ans = max(ans, self.isPalindrome(s, i, i + 1))

        return s[ans[1] : ans[1] + ans[0]]

    def isPalindrome(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                left -= 1
                right += 1
            else:
                break

        return (right - left - 1, left + 1)






        #####
        if not s:
            return ''

        ans = (1, 0)
        for i in range(len(s)):
            ans = max(ans, self.isPalindrome(s, i, i))
            ans = max(ans, self.isPalindrome(s, i, i + 1))

        return s[ans[1]: ans[1] + ans[0]]

    def isPalindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (j - i - 1, i + 1)
