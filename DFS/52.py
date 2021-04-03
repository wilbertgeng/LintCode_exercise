"""52 · Next Permutation"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    def nextPermutation(self, nums):
        # write your code here
        n = len(nums)
        if n <= 1:
            return nums

        i = n - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        if i != 0:
            j = n - 1
            while nums[i - 1] >= nums[j]:
                j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        self.swapList(nums, i, n - 1)

        return nums

S = Solution()

A = S.nextPermutation([1, 2,4,3,6,5])
print(A)
