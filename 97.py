"""97. Maximum Depth of Binary Tree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return 0 

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        return max(left, right) + 1
