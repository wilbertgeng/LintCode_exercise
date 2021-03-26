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
