"""689 · Two Sum IV - Input is a BST"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: : the root of tree
    @param: : the target sum
    @return: two numbers from tree which sum is n
    """

    def twoSum(self, root, n):
        # write your code here
        if not root:
            return None
        self.res = []
        nodes = set()
        self.dfs(root, n, nodes)
        return self.res

    def dfs(self, node, target, nodes):
        if not node:
            return

        self.dfs(node.left, target, nodes)
        if target - node.val not in nodes:
            nodes.add(node.val)
        else:
            self.res = [node.val, target - node.val]

        self.dfs(node.right, target, nodes)
