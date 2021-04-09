"""859 · Max Stack"""
class MaxStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []
        self.max_stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.stack.append(x)
        if self.max_stack and x < self.max_stack[-1]:
            self.max_stack.append(self.max_stack[-1])
        else:
            self.max_stack.append(x)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        self.max_stack.pop()
        return self.stack.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.stack[-1]

    """
    @return: An integer
    """
    def peekMax(self):
        # write your code here
        return self.max_stack[-1]

    """
    @return: An integer
    """
    def popMax(self):
        # write your code here
        number = self.max_stack.pop()
        temp = []
        while number != self.stack[-1]:
            temp.append(self.stack.pop())
        self.stack.pop()
        while temp:
            self.stack.append(temp.pop())
        return number









###
