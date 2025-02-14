"""1246. Longest Repeating Character Replacement
"""
class Solution:
    """
    @param s: a string
    @param k: a integer
    @return: return a integer
    """
    def characterReplacement(self, s, k):
        # write your code here
        d = {}
        cnt = 0

        n = len(s)
        if not s:
            return 0
        j = 0
        longest = 1
        max_freq = 0
        for i in range(n):
            while j < n and j - i - max_freq <= k:
                d[s[j]] = d.get(s[j], 0) + 1
                max_freq = max(max_freq, d[s[j]])
                j += 1
            if j - i - max_freq > k:
                longest = max(longest, j - i - 1)
            if j - i - max_freq <= k:
                longest = max(longest, j - i )
            d[s[i]] -= 1
            max_freq = max(d.values())

        return longest




        ###
        counter = {}
        max_freq = 0
        j = 0
        n = len(s)
        ans = 0
        for i in range(n):
            while j < n and j - i - max_freq <= k:
                counter[s[j]] = counter.get(s[j], 0) + 1
                max_freq = max(max_freq, counter[s[j]])
                j += 1

            if j - i - max_freq > k:
                ans = max(ans, j - i - 1)
            else:
                ans = max(ans, j - i)
            counter[s[i]] -= 1
            max_freq = max(counter.values())

        return ans
