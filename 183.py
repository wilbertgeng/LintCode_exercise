"""183. Wood Cut"""
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        # binary search find last position, because
        # we wanna find largest length of small wood
        ## Practice:
        total = sum(L)
        if k > total:
            return 0

        start = 1
        end = total // k

        while start + 1 < end:
            mid = (start + end) // 2
            if self.numPieces(mid, L) >= k:
                start = mid
            else:
                end = mid

        if self.numPieces(end, L) >= k:
            return end
        if self.numPieces(start, L) >= k:
            return start

    def numPieces(self, woodLen, L):
        res = 0
        for l in L:
            res += (l // woodLen)

        return res











        #####
        if not L or sum(L) < k: ## !!
            return 0

        start = 1
        end = min(max(L), sum(L) // k)

        while start + 1 < end:
            mid = (start + end) // 2
            if self.getPieces(L, mid) >= k:
                start = mid
            else:
                end = mid

        if self.getPieces(L, end) >= k:
            return end
        if self.getPieces(L, start) >= k:
            return start

        return 0

    def getPieces(self, L, length):
        return sum(l // length for l in L)
