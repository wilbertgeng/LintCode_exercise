"""1512 · Minimum Cost to Hire K Workers"""
class Solution:
    """
    @param quality: an array
    @param wage: an array
    @param K: an integer
    @return: the least amount of money needed to form a paid group
    """
    def mincostToHireWorkers(self, quality, wage, K):
        # Write your code here
        workers = []
        for i in range(len(quality)):
            workers.append((float(wage[i]) / quality[i], quality[i]))

        workers.sort()
        res = float("inf")
        import heapq
        heap = []
        qsum = 0
        for w, q in workers:
            heapq.heappush(heap, -q)
            qsum += q
            if K < len(heap):
                qsum += heapq.heappop(heap)
            if K == len(heap):
                res = min(res, qsum * w)

        return res 
