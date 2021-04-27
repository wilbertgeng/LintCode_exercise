"""138. Subarray Sum"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        sum_to_idx = {0: -1}
        prefix_sum = 0
        for idx, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in sum_to_idx:
                return sum_to_idx[prefix_sum] + 1, i

            sum_to_idx[prefix_sum] = i
        return -1, -1






        ###
        sum2index = {0: -1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum in sum2index:
                return sum2index[prefix_sum] + 1, i

            sum2index[prefix_sum] = i

        return -1, -1
