"""18. Subsets II"""
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(list(path))
        if index == len(nums):
            return

        for i in range(index, len(nums)):
            if i != index and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            self.dfs(nums, i + 1, path, res)
            path.pop()


        ### use hash to remove repeated
        res = []
        visited = set()
        nums.sort()
        self.dfs(nums, 0, [], visited, res)
        return res 

    def getHash(self, path):
        path = "".join([str(num) for num in path])
        return path

    def dfs(self, nums, index, path, visited, res):
        path_hash = self.getHash(path)
        if path_hash in visited:
            return

        visited.add(path_hash)
        res.append(list(path))
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, visited, res)
            path.pop()














######
