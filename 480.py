"""480. Binary Tree Paths"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        if not root:
            return []

        paths = []
        self.findPaths(root, [root.val], paths)

        return paths

    def findPaths(self, node, path, paths):
        if not node:
            return

        if not node.left and not node.right:
            paths.append('->'.join([str(n) for n in path]))
            return

        if node.left: ## !! .val doesn't work with None type 
            path.append(node.left.val)
            self.findPaths(node.left, path, paths)
            path.pop()
        if node.right:
            path.append(node.right.val)
            self.findPaths(node.right, path, paths)
            path.pop()













##
