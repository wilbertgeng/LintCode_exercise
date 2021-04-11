"""153 · Combination Sum II"""
class Solution:
    """
    @param num: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, num, target):
        # write your code here
        if not num:
            return []

        num.sort()
        res = []
        self.dfs(num, target, 0, [], res)
        return res

    def dfs(self, num, target, path_sum, path, res):
        if path_sum == target:
            res.append(list(path))
            return
        if not num or path_sum > target:
            return

        for i in range(len(num)):
            if i > 0 and num[i] == num[i - 1]:
                continue
            path.append(num[i])
            path_sum += num[i]
            self.dfs(num[i + 1:], target, path_sum, path, res)
            path_sum -= num[i]
            path.pop()
