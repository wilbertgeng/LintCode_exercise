"""90. k Sum II
"""
class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        A.sort()
        res = []
        self.dfs(A, 0, [], k, target, res)
        return res

    def dfs(self, A, index, path, k, target, res):
        if target == 0 and k == 0:
            res.append(list(path))
            return
        if k == 0:
            return

        for i in range(index, len(A)):
            if target < A[i]:
                break
            path.append(A[i])
            self.dfs(A, i + 1, path, k - 1, target - A[i], res)
            path.pop()
