"""7. Serialize and Deserialize Binary Tree
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
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if not root:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            node = queue[index]
            index += 1
            if node:
                queue.append(node.left)
                queue.append(node.right)

        while not queue[-1]:
            queue.pop()
        return "{%s}" % ",".join([str(node.val) if node is not None else '#' for node in queue])


    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        if data == "{}":
            return None

        vals = data[1:-1].split(',')
        root = TreeNode(int(vals[0]))
        isLeftChild = True
        index = 0
        queue = [root]
        for val in vals[1:]:
            node = queue[index]
            if val != "#":
                if isLeftChild:
                    node.left = TreeNode(int(val))
                    queue.append(node.left)
                else:
                    node.right = TreeNode(int(val))
                    queue.append(node.right)
            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root







###
