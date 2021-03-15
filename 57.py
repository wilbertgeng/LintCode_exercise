"""57. 3Sum"""

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        ###  Practice:
        numbers.sort()
        res = []
        n = len(numbers)
        for i in range(n - 2):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            self.twoSum(numbers, i + 1, n - 1, - numbers[i], res)

        return res

    def twoSum(self, numbers, left, right, target, res):
        lastPair = None
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target: ## !! use two ifs
                if (numbers[left], numbers[right]) != lastPair:
                    res.append([- target, numbers[left], numbers[right]])  ## !! don't miss brackets
                lastPair = (numbers[left], numbers[right])
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1




        ### Practice:
        numbers.sort()
        res = []

        for i in range(len(numbers) - 2):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue
            l = i + 1
            r = len(numbers) - 1
            while l < r:
                s = numbers[i] + numbers[l] + numbers[r]
                if l < r and s == 0:
                    res.append([numbers[i], numbers[l], numbers[r]])
                    while l < r and numbers[l] == numbers[l + 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                if l < r and s < 0:
                    l += 1
                if l < r and s > 0:
                    r -= 1

        return res

        # write your code here
        nums.sort()
        res = []
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r :
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l< r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1

        return res











######
