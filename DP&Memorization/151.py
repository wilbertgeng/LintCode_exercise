"""151 · Best Time to Buy and Sell Stock III"""
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        A0 = 0
        B0 = float('-inf')
        A1 = 0
        B1 = float('-inf')

        for price in prices:
            A1 = max(A1, B1 + price)
            B1 = max(B1, A0 - price)

            A0 = max(A0, B0 + price)
            B0 = max(B0, - price)

        return A1

        
