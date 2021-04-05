"""839 · Merge Two Sorted Interval Lists"""
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        if not list1 or not list2:
            return list1 or list2

        intervals = []
        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.pushBack(intervals, list1[i])
                i += 1
            else:
                self.pushBack(intervals, list2[j])
                j += 1

        while i < len(list1):
            self.pushBack(intervals, list1[i])
            i += 1
        while j < len(list2):
            self.pushBack(intervals, list2[j])
            j += 1

        return intervals

    def pushBack(self, intervals, interval):
        if not intervals:
            intervals.append(interval)
            return

        last_interval = intervals[-1]
        if interval.start > last_interval.end:
            intervals.append(interval)
            return
        else:
            intervals[-1].end = max(interval.end, intervals[-1].end)
            return














####
