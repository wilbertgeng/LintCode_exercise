"""915 · Inorder Predecessor in BST"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param p: the given node
    @return: the in-order predecessor of the given node in the BST
    """
    def inorderPredecessor(self, root, p):
        # write your code here
        predecessor = None
        while root:
            if p.val <= root.val:
                root = root.left
            else:
                if not predecessor or root.val > predecessor.val:
                    predecessor = root
                root = root.right

        return predecessor







        ####
        self.res = float('-inf')

        self.dfs(root, p)

        return TreeNode(self.res) if self.res != float('-inf') else None

    def dfs(self, node, p):
        if not node:
            return
        self.dfs(node.left, p)
        if self.res < node.val < p.val:
            self.res = node.val
        self.dfs(node.right, p)
