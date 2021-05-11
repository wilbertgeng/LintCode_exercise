"""140 · Fast Power"""
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # write your code here
        if b == 1:
          return 0
        if n == 0:
            return 1
        if n % 2 == 0:
            ans = self.fastPower(a, b, n // 2)
            return ans * ans % b
        else:
            ans = self.fastPower(a, b, n // 2)
            return ans * ans * a % b 
