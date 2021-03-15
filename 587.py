"""587. Two Sum - Unique pairs
"""

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        ### Practice:
        d = {}
        nums.sort()
        cnt = 0
        for i in range(len(nums)):
            if target - nums[i] in d and nums[i] not in d:
                cnt += 1
            d[nums[i]] = d.get(nums[i], 0) + 1

        for num in d: ### Be careful!! d not nums, to avoid repeated element
            if target - num == num and d[num] > 1:
                cnt += 1

        return cnt




        ####
        nums.sort()
        d = {}
        cnt = 0
        for i in range(len(nums)):
            if (target - nums[i]) in d and nums[i] not in d:
                cnt += 1
            d[nums[i]] = d.get(nums[i], 0) + 1

        for num in d:
            if num == target - num and d[num] > 1:
                cnt += 1

        return cnt
