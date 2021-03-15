"""628. Maximum Subtree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def findSubtree(self, root):
        # write your code here
        ## Divide Conquer
        self.sumMax = float('-inf')
        self.root_max = None
        self.dfs(root)
        return self.root_max

    def dfs(self, node):
        if not node:
            return 0

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if left + right + node.val >= self.sumMax or not self.root_max:
            self.sumMax = left + right + node.val
            self.root_max = node

        return left + right + node.val 
