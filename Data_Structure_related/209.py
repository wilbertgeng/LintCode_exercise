"""209 · First Unique Character in a String"""
class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        dict = {}

        for l in str:
            dict[l] = dict.get(l, 0) + 1

        for l in str:
            if dict[l] == 1:
                return l
