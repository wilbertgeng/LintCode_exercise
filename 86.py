"""
86. Binary Search Tree Iterator"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0
    """
    @return: return next node
    """
    def _next(self):
        # write your code here
        node = self.stack[-1]
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return node

    ## A simple way
    def __init__(self, root):
        self.stack = []
        self.findLeftNodes(root)

    def findLeftNodes(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def hasNext(self):
        return bool(self.stack)

    def _next(self):
        node = self.stack.pop()
        if node.right:
            self.findLeftNodes(node.right)
        return node

            






####
