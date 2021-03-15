"""492. Implement Queue by Linked List"""
class listNode(object):
    def __init__(self, val, next = None):
        self.val = val
        self.next = None

class MyQueue:
    """
    @param: item: An integer
    @return: nothing
    """
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        # write your code here
        if self.first is None:
            self.first = listNode(item)
            self.last = self.first
        else:
            self.last.next = listNode(item)
            self.last = self.last.next
    """
    @return: An integer
    """
    def dequeue(self):
        # write your code here
        if self.first is None:
            return -1
        else:
            item = self.first.val
            self.first = self.first.next
            return item
