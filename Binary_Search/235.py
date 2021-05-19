"""235 · Prime Factorization"""
class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        prime_max = int(num ** 0.5 + 1)

        res = []
        for i in range(2, prime_max):
            while num % i == 0:
                num /= i
                res.append(i)
        if num != 1:
            res.append(int(num))

        return res 
