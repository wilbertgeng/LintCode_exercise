"""486 · Merge K Sorted Arrays"""
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        if not arrays:
            return []

        if len(arrays) == 1:
            return arrays[0]

        n = len(arrays)
        mid = n // 2

        left = self.mergekSortedArrays(arrays[:mid])
        right = self.mergekSortedArrays(arrays[mid:])

        i = 0
        j = 0

        res = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1

        if i < len(left):
            res += left[i:]
        if j < len(right):
            res += right[j:]
        return res
