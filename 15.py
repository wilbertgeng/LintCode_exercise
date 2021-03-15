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
