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
        ### Practice
        return self.dfs(root)

    def dfs(self, node):
        if not node:
            return None
        last_node_left = self.dfs(node.left)
        last_node_right = self.dfs(node.right)
        if node.left:
            last_node_left.right = node.right
            node.right = node.left
            node.left = None

        return last_node_right or last_node_left or node










        ##
        if not root:
            return None

        self.dfs(root)

    def dfs(self, node):
        if not node:
            return None

        last_left_node = self.dfs(node.left)
        last_right_node = self.dfs(node.right)

        if node.left:
            last_left_node.right = node.right
            node.right = node.left
            node.left = None

        return last_right_node or last_left_node or node









        ######
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
