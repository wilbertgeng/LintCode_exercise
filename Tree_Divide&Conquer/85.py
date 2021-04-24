"""85 · Insert Node in a Binary Search Tree"""
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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        return self.dfs(root, node)

    def dfs(self, root, node):
        if not root:
            return node

        if node.val > root.val:
            root.right = self.dfs(root.right, node)
        else:
            root.left = self.dfs(root.left, node)

        return root
            
