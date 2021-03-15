"""453. Flatten Binary Tree to Linked List
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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flatten_and_return_last_node(root)

    def flatten_and_return_last_node(self, node):
        if not node:
            return None 

        last_left_node = self.flatten_and_return_last_node(node.left)
        last_right_node = self.flatten_and_return_last_node(node.right)

        if node.left is not None:
            last_left_node.right = node.right
            node.right = node.left
            node.left = None

        return last_right_node or last_left_node or node
