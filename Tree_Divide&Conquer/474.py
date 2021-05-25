"""474. Lowest Common Ancestor II
"""
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        ## Practice:
        A_parents = set()
        A_parents.add(A)
        while A != root:
            A = A.parent
            A_parents.add(A)

        while B:
            if B in A_parents:
                return B
            B = B.parent
        return None


        ####
        mapA = set()
        mapA.add(A)
        while A != root:
            A = A.parent
            mapA.add(A)

        while B != root:
            if B in mapA:
                return B
            B = B.parent

        return root
