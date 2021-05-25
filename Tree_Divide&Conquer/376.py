"""376 · Binary Tree Path Sum"""
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
    def binaryTreePathSum(self, root, target):
        # write your code here
        ## Practice:
        if not root:
            return []

        res = []
        self.dfs(root, target, [root.val], res, root.val)
        return res

    def dfs(self, node, target, path, res, path_sum):
        if not node.left and not node.right and path_sum == target:
            res.append(list(path))
            return
        if node.left:
            path.append(node.left.val)
            self.dfs(node.left, target, path, res, path_sum + node.left.val)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.dfs(node.right, target, path, res, path_sum + node.right.val)
            path.pop()


        ###
        if not root:
            return []

        res = []
        self.dfs(root, 0, target, res, [])
        return res

    def dfs(self, node, length, target, res, path):
        if not node:
            return

        length += node.val
        path.append(node.val)
        if length == target and not node.left and not node.right:
            res.append(list(path))

        self.dfs(node.left, length, target, res, path)
        self.dfs(node.right, length, target, res, path)
        path.pop()
