"""272. Climbing Stairs II
"""
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """
    def climbStairs2(self, n):
        # write your code here
        if n == 0: ## 0 is 1 step 
            return 1
        if n <= 2:
            return n

        last_two_step = 1
        last_step = 1
        step = 2

        for i in range(n - 2):
            last_two_step, last_step, step = last_step, step, last_two_step + last_step + step

        return step
