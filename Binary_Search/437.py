"""437. Copy Books
"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        ### DP: O(N^2*k)
        n = len(pages)
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

        for j in range(k + 1):
            dp[0][j] = 0

        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + pages[i - 1]

        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for prev in range(i):
                    cost = prefix_sum[i] - prefix_sum[prev]
                    dp[i][j] = min(dp[i][j], max(dp[prev][j - 1], cost))

        return dp[n][k]






        ### Practice: O(nlogSum)
        start = 0
        end = sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.numOfCopiers(pages, mid) > k:
                start = mid
            else:
                end = mid

        if self.numOfCopiers(pages, start) <= k:
            return start
        return end

    def numOfCopiers(self, pages, limit):
        num_of_copiers = 0
        lastCopy = limit

        for page in pages:
            if page > limit:  ## !!! Be careful to think about this !
                return float('inf')
            if lastCopy + page > limit:
                num_of_copiers += 1
                lastCopy = 0

            lastCopy += page

        return num_of_copiers




        ###
        start = 0
        end = sum(pages)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.numOfCopiers(pages, mid) > k:
                start = mid
            else:
                end = mid

        if self.numOfCopiers(pages, start) <= k:
            return start

        return end

    def numOfCopiers(self, pages, limit):
        num_of_copiers = 0
        pages_copied_last_time = limit

        for page in pages:
            if page > limit:
                return float('inf')
            if pages_copied_last_time + page > limit:
                num_of_copiers += 1
                pages_copied_last_time = 0

            pages_copied_last_time += page

        return num_of_copiers
