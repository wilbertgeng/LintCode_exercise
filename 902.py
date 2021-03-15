"""902. Kth Smallest Element in a BST
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        stack = []

        while root != None:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            node = stack[-1]
            if node.right is None:
                node = stack.pop()
                while len(stack) != 0 and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return stack[-1].val


####
        stack = []

        while root:
            stack.append(root)
            root = root.left

        for _ in range(k - 1):
            node = stack[-1]

            if node.right is None:
                node = stack.pop()
                while len(stack) != 0 and stack[-1].right == node:
                    node = stack.pop()
            else:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
        return stack[-1].val 










###
