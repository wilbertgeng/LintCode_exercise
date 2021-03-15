"""143. Sort Colors II
彩虹排序
"""
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        ## k次partition，每次划分出一种颜色	O(nk)	O(1)
        for i in range(1, k + 1):
            left = 0
            right = len(colors) - 1
            while left <= right:
                while left <= right and colors[left] <= i:
                    left += 1
                while left <= right and colors[right] > i:
                    right -= 1

                if left <= right:
                    colors[left], colors[right] = colors[right], colors[left]
                    left += 1
                    right -= 1

        ## 分治法，logk次 partition（最优）	O(nlogk)	O(logk)
        self.partition(colors, 1, k, 0, len(colors) - 1)

    def partition(self, colors, color_from, color_to, idx_from, idx_to):
        if color_from == color_to or idx_from == idx_to:
            return

        color = (color_from + color_to) // 2
        left, right = idx_from, idx_to
        while left <= right:
            while left <= right and colors[left] <= color:
                left += 1
            while left <= right and colors[right] > color:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.partition(colors, color_from, color, idx_from, right)
        self.partition(colors, color + 1, color_to, left, idx_to)
