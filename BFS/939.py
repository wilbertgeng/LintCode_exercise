"""939. Binary Tree Kth Floor Node
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
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloorNode(self, root, k):
        # Write your code here
        ## Practice:
        if not root:
            return 0

        queue = collections.deque([root])
        level_num_nodes = 1
        level = 0

        while queue:
            level += 1
            if level == k:
                return level_num_nodes
            level_num_nodes = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_num_nodes += 1
                if node.right:
                    queue.append(node.right)
                    level_num_nodes += 1
        return 0



        #######
        if not root:
            return 0

        queue = collections.deque([root])
        level = 0
        level_num_nodes = 1
        while queue:
            level += 1
            if level == k:
                return level_num_nodes
            level_num_nodes = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    level_num_nodes += 1
                if node.right:
                    queue.append(node.right)
                    level_num_nodes += 1
