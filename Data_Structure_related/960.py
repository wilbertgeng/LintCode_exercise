"""960 · First Unique Number in Data Stream II"""
class DataStream:

    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.counter = {}
        self.dict = set()

    """
    @param num: next number in stream
    @return: nothing
    """
    def add(self, num):
        # write your code here
        if num not in self.dict:
            self.dict.add(num)
            self.nums.append(num)
        self.counter[num] = self.counter.get(num, 0) + 1

    """
    @return: the first unique number in stream
    """
    def firstUnique(self):
        # write your code here
        for num in self.nums:
            if self.counter[num] == 1:
                return num
        return None
