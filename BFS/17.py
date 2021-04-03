"""17. Subsets
"""
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        res = []
        n = len(nums)
        nums.sort()
        for i in range(1 << n):
            subset = []
            for j in range(n):
                if (i & (1 << j)) != 0:
                    subset.append(nums[j])
            res.append(subset)

        return res


        ### BFS1 practice
        res = []
        queue = [[]]
        index = 0

        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and num <= subset[-1]:
                    continue
                queue.append(subset + [num])
        return queue

        ### BFS 2 practice
        nums.sort()
        res = [[]]

        for i in range(len(nums)):
            for j in range(len(res)):
                res.append(res[j] + [nums[i]])

        return res

        ### DFS practice:
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


        ### BFS 1:
        queue = [[]]
        index = 0
        if not nums:
            return [[]]

        while index < len(queue):
            subset = queue[index]
            index += 1
            for num in nums:
                if subset and subset[-1] >= num:
                    continue
                queue.append(subset + [num])

        return queue

        ### BFS 2:
        queue = [[]]
        if not nums:
            return [[]]

        for num in sorted(nums):
            for i in range(len(queue)):
                subset = list(queue[i])
                queue.append(subset + [num])

        return queue

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
