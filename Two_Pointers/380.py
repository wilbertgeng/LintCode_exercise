"""380. Intersection of Two Linked Lists
"""
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        A = headA
        B = headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA

        return A
