"""1879 · Two Sum VII"""
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
    """
    def twoSumVII(self, nums, target):
        # write your code here
        d = {}

        res = []
        for idx, num in enumerate(nums):
            if target - num in d:
                res.append([d[target - num], idx])
            d[num] = idx

        return res
        
