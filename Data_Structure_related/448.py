"""448 · Inorder Successor in BST"""
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root:
            if p.val >= root.val:
                root = root.right
            else:
                if not successor or root.val < successor.val:
                    successor = root
                root = root.left

        return successor 
