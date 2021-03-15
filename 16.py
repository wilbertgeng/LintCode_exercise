"""
16. Permutations II
"""
class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        res = []
        visited = [False] * len(nums)
        self.dfs(nums, res, [], visited)
        return res

    def dfs(self, nums, res, path, visited):
        if len(nums) == len(path):
            res.append(list(path))
            return

        for i in range(len(nums)):
            if visited[i]:
                continue
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue
            visited[i] = True
            path.append(nums[i])
            self.dfs(nums, res, path, visited)
            visited[i] = False
            path.pop()
