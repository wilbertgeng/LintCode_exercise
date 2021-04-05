"""577 · Merge K Sorted Interval Lists"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        # write your code here
        n = len(intervals)
        if n == 0:
            return []
        if n == 1:
            return intervals[0]

        mid = n // 2

        left = self.mergeKSortedIntervalLists(intervals[:mid])
        right = self.mergeKSortedIntervalLists(intervals[mid:])

        i = 0
        j = 0
        
        res = []
        while i < len(left) and j < len(right):
            if left[i].start < right[j].start:
                self.pushBack(res, left[i])
                i += 1
            else:
                self.pushBack(res, right[j])
                j += 1

        while i < len(left):
            self.pushBack(res, left[i])
            i += 1
        while j < len(right):
            self.pushBack(res, right[j])
            j += 1

        return res

    def pushBack(self, intervals_prev, interval):
        if not intervals_prev:
            intervals_prev.append(interval)
            return
        last_interval = intervals_prev[-1]
        if interval.start <= last_interval.end:
            intervals_prev[-1].end = max(intervals_prev[-1].end, interval.end)
            return
        else:
            intervals_prev.append(interval)
            return
