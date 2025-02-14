"""134. LRU Cache
"""
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self._remove(node)
        self._add(node)
        return node.val

    def set(self, key, value):
        if key in self.dict:
            self._remove(self.dict[key])
        node = Node(key, value)
        self.dict[key] = node
        self._add(node)
        if len(self.dict) > self.capacity:
            n = self.head.next ## be carefull！！
            self._remove(n)
            del self.dict[n.key]

    def _add(self, node):
        n = self.tail.prev
        n.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = n

    def _remove(self, node):
        n = node.next
        node.prev.next = n
        n.prev = node.prev





#####
class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.dict = {}

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.dict:
            return -1
        n = self.dict[key]
        self._remove(n)
        self._add(n)
        return n.val

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.dict:
            self._remove(self.dict[key])
        n = Node(key, value)
        self._add(n)
        self.dict[key] = n
        if len(self.dict) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dict[n.key]

    def _add(self, node):
        n = self.tail.prev
        n.next = node
        node.prev = n
        node.next = self.tail
        self.tail.prev = node

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
