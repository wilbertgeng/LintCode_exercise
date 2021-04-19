"""40 · Implement Queue by Two Stacks"""
class MyQueue:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.stack2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if not self.stack2:
            self.stack1To2(self.stack, self.stack2)
            return self.stack2.pop()
        else:
            return self.stack2.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if not self.stack2:
            self.stack1To2(self.stack, self.stack2)
            return self.stack2[-1]
        else:
            return self.stack2[-1]

    def stack1To2(self, stack1, stack2):
        while stack1:
            stack2.append(stack1.pop())
