"""93. Balanced Binary Tree
"""
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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        is_balanced, height = self.divideConquer(root)
        return is_balanced

    def divideConquer(self, node):
        if not node:
            return True, 0

        left_is_balanced, left_height = self.divideConquer(node.left)
        right_is_balanced, right_height = self.divideConquer(node.right)
        height = max(left_height, right_height) + 1

        if not left_is_balanced or not right_is_balanced:
            return False, height
        if abs(left_height - right_height) > 1:
            return False, height
        return True, height









####
