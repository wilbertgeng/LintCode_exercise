"""425. Letter Combinations of a Phone Number
"""
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        ## Practice:
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        res = []
        self.dfs(digits, 0, "", res, digits_map)
        return res

    def dfs(self, digits, idx, path, res, digits_map):
        if idx == len(digits):
            res.append(path)
            return

        for l in digits_map[digits[idx]]:
            self.dfs(digits, idx + 1, path + l, res, digits_map)



        ###
        digits_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        if not digits:
            return []
        res = []
        self.dfs(digits, 0, "", digits_map, res)
        return res

    def dfs(self, digits, index, path, digits_map, res):
        if index == len(digits):
            res.append(path)
            return

        for letter in digits_map[digits[index]]:
            path += letter
            self.dfs(digits, index + 1, path, digits_map, res)
            path = path[:-1]

    #####
        """ use list for path instead of string, then use append, pop, "".join(path) """

















    ########
