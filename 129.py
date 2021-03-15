"""129. Rehashing"""
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        HASH_SIZE = 2 * len(hashTable)
        ans_hashTable = [None for _ in range(HASH_SIZE)]
        for item in hashTable:
            p = item
            while p:
                self.addNode(ans_hashTable, p.val)
                p = p.next

        return ans_hashTable

    def addNode(self, ans_hashTable, num):
        p = num % len(ans_hashTable)
        if ans_hashTable[p]:
            self.addListNode(ans_hashTable[p], num)
        else:
            ans_hashTable[p] = ListNode(num)

    def addListNode(self, node, num):
        if node.next:
            self.addListNode(node.next, num)
        else:
            node.next = ListNode(num)














######
