"""175 · Invert Binary Tree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        return self.invert(root)

    def invert(self, node):
        if not node:
            return None

        left = self.invert(node.right)
        right = self.invert(node.left)

        node.left = left
        node.right = right

        return node
