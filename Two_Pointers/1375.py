"""1375. Substring With At Least K Distinct Characters
"""
class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """
    def kDistinctCharacters(self, s, k):
        # Write your code here
        if len(set(s)) < k:
            return 0

        ans = 0
        count = {}
        n = len(s)
        j = 0

        for i in range(n):
            while j < n and len(count) < k:
                count[s[j]] = count.get(s[j], 0) + 1
                j += 1
            if len(count) >= k:
                ans += n - j + 1
            count[s[i]] -= 1
            if count[s[i]] == 0:
                del count[s[i]]

        return ans
