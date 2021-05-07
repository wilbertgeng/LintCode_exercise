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
        n = len(s)
        if n < k:
            return 0

        cnt = 0
        store = set()
        for i in range(n - k + 1):
            store.add(s[i])
            j = i + 1
            while len(store) < k and j < n:
                store.add(s[j])
                j += 1
            if len(store) >= k:
                cnt += n - j + 1
            store = set()
        return cnt

        ## optimize
        n = len(s)
        if n < k:
            return 0

        cnt = {}
        ans = 0
        j = 0
        for i in range(n):
            while len(cnt) < k and j < n:
                cnt[s[j]] = cnt.get(s[j], 0) + 1
                j += 1

            if len(cnt) >= k:
                ans += n - j + 1
            cnt[s[i]] -= 1
            if cnt[s[i]] == 0:
                del cnt[s[i]]

        return ans





        ###
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
