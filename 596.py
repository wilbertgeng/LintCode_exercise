"""596. Minimum Subtree"""
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
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        root_min, sum_sub, sum_min = self.getTreeSum(root)
        return root_min

    def getTreeSum(self, node):
        if not node:
            return None, 0, 0

        left_root, left_sum, left_sum_min = self.getTreeSum(node.left)
        right_root, right_sum, right_sum_min = self.getTreeSum(node.right)

        root_sum = left_sum + right_sum + node.val

        if left_sum_min == min(left_sum_min, right_sum_min, root_sum):
            return left_root, root_sum, left_sum_min
        if right_sum_min == min(right_sum_min, left_sum_min, root_sum):
            return right_root, root_sum, right_sum_min
        return node, root_sum, root_sum
