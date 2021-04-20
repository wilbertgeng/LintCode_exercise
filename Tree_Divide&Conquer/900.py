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
        ### Practice:
        up = root
        low = root

        while root:
            if root.val > target:
                up = root
                root = root.left
            elif root.val < target:
                low = root
                root = root.right
            else:
                return root.val

        if abs(up.val - target) < abs(target - low.val):
            return up.val
        return low.val




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

        if (upper.val - target) < (target - lower.val):
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
