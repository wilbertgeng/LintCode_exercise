"""494 · Implement Stack by Two Queues"""
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue = collections.deque([])
        self.queue_tmp = collections.deque([])
    def push(self, x):
        # write your code here
        self.queue.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        for _ in range(len(self.queue) - 1):
            self.queue_tmp.append(self.queue.popleft())
        self.queue.popleft()
        self.queue, self.queue_tmp = self.queue_tmp, self.queue

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        for _ in range(len(self.queue) - 1):
            self.queue_tmp.append(self.queue.popleft())
        val = self.queue[0]
        self.queue_tmp.append(self.queue.popleft())
        self.queue, self.queue_tmp = self.queue_tmp, self.queue
        return val

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return not self.queue 
