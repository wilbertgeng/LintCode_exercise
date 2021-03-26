"""17. Subsets
"""
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        

        ###
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(list(path))
        if index == len(nums):
            return

        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()
##

        ####
        nums.sort()
        res = []
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self  , nums, index, path, res):
        if index == len(nums):
            res.append(list(path)) ## !! dont't forget list. hard copy
            return

        path.append(nums[index])
        self.dfs(nums, index + 1, path, res)

        path.pop()
        self.dfs(nums, index + 1, path, res)
