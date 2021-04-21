"""597 · Subtree with Maximum Average"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        max_node, node_avg_max, node_sum, node_num = self.dfs(root)

        return max_node

    def dfs(self, node):
        if not node:
            return None, float('-inf'), 0, 0

        l_max_node, l_node_avg_max, l_node_sum, l_node_num = self.dfs(node.left)
        r_max_node, r_node_avg_max, r_node_sum, r_node_num = self.dfs(node.right)

        node_sum = l_node_sum + r_node_sum + node.val
        node_num = l_node_num + r_node_num + 1
        node_avg = node_sum / node_num

        if node_avg > l_node_avg_max and node_avg > r_node_avg_max:
            return node, node_avg, node_sum, node_num
        if l_node_avg_max == max(l_node_avg_max, r_node_avg_max, node_avg):
            return l_max_node, l_node_avg_max, node_sum, node_num
        if r_node_avg_max == max(l_node_avg_max, r_node_avg_max, node_avg):
            return r_max_node, r_node_avg_max, node_sum, node_num
