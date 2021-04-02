"""基本操作之删除(Delete)
思路(最为复杂)
考虑待删除的节点为叶子节点，可以直接删除并修改父亲节点(Parent Node)的指针，需要区分待删节点是否为根节点
考虑待删除的节点为单支节点(只有一棵子树——左子树 or 右子树)，与删除链表节点操作类似，同样的需要区分待删节点是否为根节点
考虑待删节点有两棵子树，可以将待删节点与左子树中的最大节点进行交换，由于左子树中的最大节点一定为叶子节点，所以这时再删除待删的节点可以参考第一条
详细的解释可以看 http://www.algolist.net/Data_structures/Binary_search_tree/Removal"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def removeNode(root, value):
        dummy = TreeNode(0)
        dummy.left = root
        parent = findNode(dummy, root, value)
        node = None
        if parent.left and parent.left.val == value:
            node = parent.left
        elif parent.right and parent.right.val == value:
            node = parent.right
        else:
            return dummy.left
        deleteNode(parent, node)
        return dummy.left

    def findNode(parent, node, value):
        if not node:
            return parent
        if node.val == value:
            return parent
        if value < node.val:
            return findNode(node,node.left, value)
        else:
            return findNode(node, node.right, value)

    def deleteNode(parent, node):
        if not node.right:
            if parent.left == node:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            temp = node.right
            father = node
            while temp.left:
                father = temp
                temp = temp.left
            if father.left == temp:
                father.left = temp.right
            else:
                father.right = temp.right
            if parent.left == node:
                parent.left = temp
            else:
                parent.right = temp
            temp.left = node.left
            temp.right = node.right
