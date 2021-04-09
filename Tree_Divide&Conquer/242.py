"""242 · Convert Binary Tree to Linked Lists by Depth"""
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        if not root:
            return []
        res = []

        queue = collections.deque([root])
        dummy = ListNode(0)
        last_node = None
        while queue:
            dummy.next = None
            last_node = dummy
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                node = ListNode(node.val)
                last_node.next = node
                last_node = node


            res.append(dummy.next)

        return res 
