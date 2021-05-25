"""70 · Binary Tree Level Order Traversal II"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        if not root:
            return []

        res = []
        queue = collections.deque([root])

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(temp)

        return res[::-1]



        ###
        if not root:
            return []

        queue = [[root]]
        index = 0
        res = [[root.val]]

        while index < len(queue):
            curr_level = queue[index]
            index += 1
            next_level = []
            next_level_vals = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                    next_level_vals.append(node.left.val)
                if node.right:
                    next_level.append(node.right)
                    next_level_vals.append(node.right.val)

            if next_level:
                queue.append(next_level)
                res.append(next_level_vals)

        return res[::-1]
