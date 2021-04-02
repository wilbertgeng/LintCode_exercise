"""11 · Search Range in Binary Search Tree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        if not root:
            return []
        res = []
        self.dfs(root, k1, k2, res)
        return res

    def dfs(self, node, k1, k2, res):
        if not node:
            return

        self.dfs(node.left, k1, k2, res)
        if k1 <= node.val <= k2:
            res.append(node.val)
        self.dfs(node.right, k1, k2, res)
