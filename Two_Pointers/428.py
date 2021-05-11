"""428 · Pow(x, n)"""
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # write your code here
        ## O(logn) time
        if n == 0:
            return 1
        m = abs(n)

        ans = self.partition(x, 1, m)
        return ans if n > 0 else 1 / ans

    def partition(self, x, idx_start, idx_end):
        if idx_start == idx_end:
            return x
        mid = (idx_start + idx_end) // 2
        left = self.partition(x, idx_start, mid)
        if mid - idx_start == idx_end - mid - 1:
            right = left
        else:
            right = left / x
        return left * right
