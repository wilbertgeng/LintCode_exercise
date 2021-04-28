"""612 · K Closest Points"""
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        import heapq
        heap = []
        for pt in points:
            distance = self.getDistance(pt.x, pt.y, origin)
            heapq.heappush(heap, (-distance, -pt.x, -pt.y))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            dis, x, y = heapq.heappop(heap)
            res.append(Point(-x, -y))

        return res[::-1]

    def getDistance(self, x, y, org):
        return (x - org.x) ** 2 + (y - org.y) ** 2







####
