"""366. Fibonacci
"""
class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n <= 2:
            return n - 1
        res = [0] * n
        res[0] = 0
        res[1] = 1

        for i in range(2, n):
            res[i] = res[i - 1] + res[i - 2]

        return res[n - 1]


"""
1. 递归的含义： 输入， 输出， 含义
2. 递归的拆解
3. 递归的出口
"""
