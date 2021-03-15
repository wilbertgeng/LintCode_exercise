"""900. Closest Binary Search Tree Value
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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        ##### Iteration with upper and lower bound
        upper = root
        lower = root

        while root:
            if target > root.val:
                upper = root
                root = root.right
            elif target < root.val:
                lower = root
                root = root.left
            else:
                return root.val

        if (upper.val - target) < (target - lower):
            return upper.val
        return lower.val 









        #####
        self.res = None
        if not root:
            return None
        self.diff = float('inf')

        self.search(root, target)
        return self.res

    def search(self, node, target):
        if not node:
            return

        if abs(node.val - target) < self.diff:
            self.res = node.val
            self.diff = abs(node.val - target)

        if target > node.val:
            self.search(node.right, target)
        elif target < node.val:
            self.search(node.left, target)
        else:
            self.res = node.val
            self.diff = abs(node.val - target)
            return













####
