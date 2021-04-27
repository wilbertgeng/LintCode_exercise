"""
657. Insert Delete GetRandom O(1)
"""
import random
class RandomizedSet:
    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.numToIndex = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.numToIndex:
            return False
        self.nums.append(val)
        self.numToIndex[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.numToIndex:
            return False
        index = self.numToIndex[val]
        last = self.nums[-1]
        self.nums[index] = self.nums[-1]
        self.numToIndex[last] = index
        self.nums.pop()
        del self.numToIndex[val]
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]



import random
class RandomizedSet:

    def __init__(self):
        # do intialization if necessary
        self.nums = []
        self.val2Index = {}

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        # write your code here
        if val in self.val2Index:
            return False
        self.nums.append(val)
        self.val2Index[val] = len(self.nums) - 1
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        # write your code here
        if val not in self.val2Index:
            return False
        index = self.val2Index[val]
        last = self.nums[-1]
        self.val2Index[last] = index
        self.nums[index] = last
        self.nums.pop()
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        # write your code here
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()
