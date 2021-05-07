"""56. Two Sum"""

class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here


        ###
        d = {}

        for i, num in enumerate(numbers):
            if target - num not in d:
                d[num] = i
            else:
                return [d[target - num], i]
        return [-1, -1]




        ## HashMap O(n) O(n)
        d = {}

        for i in range(len(numbers)):
            if target - numbers[i] in d: ## !! check first to avoid repeated index
                return [d[target - numbers[i]], i]
            else:
                d[numbers[i]] = i

        return [-1, -1]

        ## 2 pointers + sort O(nlogn) O(1)
        if not numbers:
            return [-1, -1]

        nums = [(num, index) for index, num in enumerate(numbers)]
        nums.sort()

        l = 0
        r = len(numbers) - 1

        while l < r:
            if nums[l][0] + nums[r][0] == target:
                return sorted(nums[l][1], nums[r][1])
            elif nums[l][0] + nums[r][0] < target:
                l += 1
            else:
                r -= 1

        return [-1, -1]
