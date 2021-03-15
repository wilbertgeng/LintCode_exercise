"""135. Combination Sum"""
class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        candidates.sort()
        res = []
        self.dfs(candidates, [], target, res, 0)
        return res

    def dfs(self, candidates,  path, target, res, index):
        if sum(path) == target:
            res.append(list(path))
            return

        for i in range(index, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            if sum(path) > target:
                path.pop()
                break
            self.dfs(candidates, path, target, res, i)
            path.pop()

#####
        candidates = sorted(list(set(candidates))) ## 用set可以去重
        results = []
        self.dfs(candidates, target, 0, [], results)
        return results

    # 递归的定义：在candidates[start ... n-1] 中找到所有的组合，他们的和为 target
    # 和前半部分的 combination 拼起来放到 results 里
    # （找到所有以 combination 开头的满足条件的组合，放到 results）
    def dfs(self, candidates, target, start, combination, results):
        # 递归的出口：target <= 0
        if target == 0:
            # deepcooy
            return results.append(list(combination))

        # 递归的拆解：挑一个数放到 combination 里
        for i in range(start, len(candidates)):
            if target - candidates[i] < 0:
                break
            # [2] => [2,2]
            combination.append(candidates[i])

            self.dfs(candidates, target - candidates[i], i, combination, results)
            # [2,2] => [2]
            combination.pop()  # backtracking







##
