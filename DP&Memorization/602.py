"""602 · Russian Doll Envelopes"""
class Solution:
    """
    @param envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        ### Practice:
        







        ######
        if not envelopes:
            return 0

        n = len(envelopes)
        lis = [float('inf')] * (n + 1)
        lis[0] = float('-inf')
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        max_layers = 0
        for w, h in envelopes:
            index = self.BiSearch_gte(lis, h)
            lis[index] = h
            max_layers = max(max_layers, index)

        return max_layers

    def BiSearch_gte(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] >= target:
            return start
        return end
