"""578. Lowest Common Ancestor III
"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        a_exist, b_exist, LCA = self.helper(root, A, B)
        if a_exist and b_exist:
            return LCA
        return None

    def helper(self, node, A, B):
        if not node:
            return False, False, None

        l_a_exist, l_b_exist, left_node = self.helper(node.left, A, B)
        r_a_exist, r_b_exist, right_node = self.helper(node.right, A, B)
        node_a_exist, node_b_exist = False, False
        if l_a_exist or r_a_exist or node == A:
            node_a_exist = True
        if l_b_exist or r_b_exist or node == B:
            node_b_exist = True
        if node == A or node == B:
            return node_a_exist, node_b_exist, node

        if left_node and right_node:
            return node_a_exist, node_b_exist, node
        if left_node:
            return node_a_exist, node_b_exist, left_node
        if right_node:
            return node_a_exist, node_b_exist, right_node
        return node_a_exist, node_b_exist, None






#####
