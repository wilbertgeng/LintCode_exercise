"""607. Two Sum III - Data structure design
"""
class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        
        self.counter = {}
    def add(self, number):
        # write your code here

        self.counter[number] = self.counter.get(number, 0) + 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        # hash 的 key 是无序的
        # vector 是动态数组
        for num1 in self.counter:
            num2 = value - num1
            if num2 == num1 and self.counter[num1] >= 2:
                return True
            if num1 != num2 and num2 in self.counter:
                return True

        return False
