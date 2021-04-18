"""570 · Find the Missing Number II"""
class Solution:
    """
    @param n: An integer
    @param str: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def findMissing2(self, n, str):
        # write your code here
        path = []
        res = []
        self.dfs(str, n, path, res)
        print(res)
        nums = res[0]
        return (1 + n) * n // 2 - sum(nums)

    def dfs(self, str, n, path, res):
        if len(path) == n - 1 and str == "":
            res.append(list(path))
            return

        for i in range(1, 3):
            if i > len(str):
                break
            num = int(str[:i])
            if num > n or num in path or str[0] == "0"):
                continue

            path.append(num)

            self.dfs(str[i:], n, path, res)
            path.pop()





        [['19', '20', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '18'],
        ['19', '20', '12', '3', '4', '5', '6', '7', '8', '9', '10', '1', '11', '2', '13', '14', '15', '16', '18'],
         ['19', '20', '12', '3', '4', '5', '6', '7', '8', '9', '10', '11', '1', '2', '13', '14', '15', '16', '18']]
