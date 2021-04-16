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
        ## Practice：
        nums.sort()
        dict = set()
        l = 0
        r = len(nums) - 1
        cnt = 0
        while l < r:
            while l < r and nums[l] + nums[r] < target:
                l += 1
            while l < r and nums[l] + nums[r] > target:
                r -= 1
            if nums[l] + nums[r] == target:
                if (nums[l], nums[r]) not in dict:
                    cnt += 1
                    dict.add((nums[l], nums[r]))
                l += 1
                r -= 1
        return cnt


        ### Practice:
        dict = {}
        cnt = 0
        for num in nums:
            if target - num in dict and num not in dict:
                cnt += 1
            dict[num] = dict.get(num, 0) + 1

        for num in nums:
            if target - num == num and dict[num] >= 2:
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
