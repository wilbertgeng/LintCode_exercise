"""109. Triangle
"""
class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """
    def minimumTotal(self, triangle):
        # write your code here
        ## Practice:
        m = len(triangle)

        for i in range(m - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]


        ###
        return self.divideConquer(triangle, 0, 0, {})

    def divideConquer(self, triangle, x, y, memo):
        if x == len(triangle):
            return 0

        if (x, y) in memo:
            return memo[(x, y)]

        left = self.divideConquer(triangle, x + 1, y, memo)
        right = self.divideConquer(triangle, x + 1, y + 1, memo)

        memo[(x, y)] = min(left, right) + triangle[x][y]

        return memo[(x, y)]

        ## DP Bottom up
        dp = list(triangle)

        n = len(triangle)
        for i in range(n - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]

        return dp[0][0]
