"""246 · Binary Tree Path Sum II"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        if not root:
            return []

        res = []
        self.dfs(root, 0, target, [], res)
        return res

    def dfs(self, node, length, target, path, res):
        if not node:
            return
        path.append(node.val)
        goal = target
        for l in range(length, -1, -1):
            goal -= path[l]
            if goal == 0:
                res.append(path[l:])

        self.dfs(node.left, length + 1, target, path, res)
        self.dfs(node.right, length + 1, target, path, res)
        path.pop()
