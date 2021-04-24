"""87 · Remove Node in Binary Search Tree"""
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
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        ### Solution 1:
        return self.dfs(root, value)

    def dfs(self, node, value):
        if not node:
            return None
        if node.val < value:
            node.right = self.dfs(node.right, value)
        elif node.val > value:
            node.left = self.dfs(node.left, value)
        else:
            if node.left and node.right:
                right_max = self.findRightMax(node)
                node.val = right_max.val
                node.left = self.dfs(node.left, right_max.val)
            elif node.left:
                node = node.left
            elif node.right:
                node = node.right
            else:
                node = None
        return node

    def findRightMax(self, node):
        node = node.left
        while node.right:
            node = node.right
        return node
