"""88. Lowest Common Ancestor of a Binary Tree
Assume two nodes are exist in tree."""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        ### Practice:

        return self.dfs(root, A, B)

    def dfs(self, node, a, b):
        if not node:
            return None 
        if node == a or node == b:
            return node

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        if not left and not right:
            return None

        if left and right:
            return node

        return left or right








        ##
        if not root:
            return None
        if root == A or root == B:
            return root

        left = self.lowestCommonAncestor(root.left, A, B)
        right = self.lowestCommonAncestor(root.right, A, B)

        if left and right:
            return root
        if left or right:
            return left or right
        return None
