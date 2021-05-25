"""1311 · Lowest Common Ancestor of a Binary Search Tree"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        ## Practice:
        if not root:
            return None
        if p.val < q.val:
            return self.dfs(root, p, q)
        return self.dfs(root, q, p)

    def dfs(self, node, p, q):
        if not node:
            return None

        if p.val <= node.val <= q.val:
            return node
        if node.val < p.val:
            return self.dfs(node.right, p, q)
        return self.dfs(node.left, p, q)


        ####
        if p.val < q.val:
            return self.dfs(root, p, q)
        return self.dfs(root, q, p)

    def dfs(self, node, p, q):
        if not node:
            return None

        if p.val <= node.val <= q.val:
            return node

        if node.val < p.val:
            return self.dfs(node.right, p, q)
        return self.dfs(node.left, p, q)
