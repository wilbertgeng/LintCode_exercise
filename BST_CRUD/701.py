"""701 · Trim a Binary Search Tree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: given BST
    @param minimum: the lower limit
    @param maximum: the upper limit
    @return: the root of the new tree
    """
    def trimBST(self, root, minimum, maximum):
        # write your code here
        if not root:
            return None

        if root.val <= maximum and root.val >= minimum:
            root.left = self.trimBST(root.left, minimum, maximum)
            root.right = self.trimBST(root.right, minimum, maximum)
            return root

        if root.val < minimum:
            return self.trimBST(root.right, minimum, maximum)
        else:
            return self.trimBST(root.left, minimum, maximum)
