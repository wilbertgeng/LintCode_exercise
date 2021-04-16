"""148. Sort Colors
"""
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        ### Practice
        r, w, b = 0, 0 , len(nums) - 1
        while w <= b:
            if nums[w] == 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
                r += 1
            if nums[w] == 1:
                w += 1
            if nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1




        ###
        r, w, b = 0, 0, len(nums) - 1

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
            elif nums[w] == 1:
                w += 1
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
