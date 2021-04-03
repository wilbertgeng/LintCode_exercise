"""15. Permutations
"""
class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        res = []
        visited = [False] * len(nums)
        self.dfs(nums,  [], visited, res)
        return res

    def dfs(self, nums,  path, visited, res):
        if len(path) == len(nums):
            res.append(list(path))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            path.append(nums[i])
            visited[i] = True
            self.dfs(nums,  path, visited, res)
            path.pop()
            visited[i] = False

        ### 非递归实现DFS
        nums.sort()
        res = []

        if len(nums) <= 1:
            return [nums]
        hasNext = True

        while hasNext:
            nums = list(nums)
            res.append(nums)
            hasNext = self.nextPermutation(nums)

        return res

    def swapList(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 1

        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            return False

        j = n - 1
        while j > 0 and nums[i - 1] >= nums[j]:
            j -= 1

        nums[i - 1], nums[j] = nums[j], nums[i - 1]

        self.swapList(nums, i, n - 1)
        return True
