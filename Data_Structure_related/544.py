"""544 · Top k Largest Numbers"""
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        import heapq
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)

        res = []
        for _ in range(k):
            num = heapq.heappop(heap)
            res.append(-num)

        return res 
