"""901. Closest Binary Search Tree Value II
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
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # write your code here
        ### O(k + logn)
        lower_stack = self.getStack(root, target)
        upper_stack = list(lower_stack)
        if lower_stack[-1].val > target:
            self.moveLower(lower_stack)
        else:
            self.moveUpper(upper_stack)

        res = []
        for i in range(k):
            if self.isLowerCloser(upper_stack, lower_stack, target):
                res.append(lower_stack[-1].val)
                self.moveLower(lower_stack)
            else:
                res.append(upper_stack[-1].val)
                self.moveUpper(upper_stack)

        return res


    def getStack(self, root, target):
        stack = []
        while root:
            if root.val > target:
                stack.append(root)
                root = root.left
            else:
                stack.append(root)
                root = root.right
        return stack

    def moveUpper(self, stack):
        if stack[-1].right:
            node = stack[-1].right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while len(stack) != 0 and stack[-1].right == node:
                node = stack.pop()

    def moveLower(self, stack):
        if stack[-1].left:
            node = stack[-1].left
            while node:
                stack.append(node)
                node = node.right
        else:
            node = stack.pop()
            while len(stack) != 0 and stack[-1].left == node:
                node = stack.pop()

    def isLowerCloser(self, upper_stack, lower_stack, target):
        if not lower_stack:
            return False
        if not upper_stack:
            return True 
        return upper_stack[-1].val - target > target - lower_stack[-1].val





        ### O(n)
        if not root or k == 0:
            return []

        nums = []
        self.inOrder(root, nums)
        left = self.findIndex(nums, target)
        right = left + 1
        res = []
        for _ in range(k):
            if self.is_left_closer(left, right, nums, target):
                res.append(nums[left])
                left -= 1
            else:
                res.append(nums[right])
                right += 1

        return res


    def inOrder(self, node, nums):
        if not node:
            return

        self.inOrder(node.left, nums)
        nums.append(node.val)
        self.inOrder(node.right, nums)
        return

    def findIndex(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[end] <= target:
            return end
        return start

    def is_left_closer(self, left, right, nums, target):
        if left < 0:
            return False
        if right >= len(nums):
            return True
        return target - nums[left] < nums[right] - target
