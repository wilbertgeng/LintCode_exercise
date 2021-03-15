"""891. Valid Palindrome II
"""
class Solution:
    """
    @param s: a string
    @return: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        ## Practice:
        if not s:
            return False

        left = 0
        right = len(s) - 1
        left, right = self.isDifferent(s, left, right)
        if left >= right:
            return True

        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isDifferent(self, s , left, right):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        return left, right

    def isPalindrome(self, s, left, right):
        left, right = self.isDifferent(s, left, right)
        return left >= right





        ###
        if not s:
            return False

        left = 0
        right = len(s) - 1

        left, right = self.isDifferent(s, left, right)
        if left >= right:
            return True

        return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)

    def isDifferent(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                break
            left += 1
            right -= 1

        return (left, right)

    def isPalindrome(self, s, left, right):
        left, right = self.isDifferent(s, left, right)
        return left >= right
