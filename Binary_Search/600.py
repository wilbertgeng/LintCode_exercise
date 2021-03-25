"""600. Smallest Rectangle Enclosing Black Pixels
"""
class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        # write your code here
        if not image or not image[0]:
            return 0

        m = len(image)
        n = len(image[0])
        left = self.findFirst(image, 0, y, self.checkColumn)
        right = self.findLast(image, y, n - 1, self.checkColumn)
        up = self.findFirst(image, 0, x, self.checkRow)
        down = self.findLast(image, x, m - 1, self.checkRow)

        return (right - left + 1) * (down - up + 1)

    def findFirst(self, image, start, end, checkFunc):
        while start + 1 < end:
            mid = (start + end) // 2
            if not checkFunc(image, mid):
                start = mid
            else:
                end = mid

        if checkFunc(image, start):
            return start
        return end

    def findLast(self, image, start, end, checkFunc):
        while start + 1 < end:
            mid = (start + end) // 2
            if not checkFunc(image, mid):
                end = mid
            else:
                start = mid

        if checkFunc(image, end):
            return end
        return start

    def checkRow(self, image, row):
        for i in range(len(image[0])):
            if image[row][i] == "1":
                return True
        return False

    def checkColumn(self, image, col):
        for i in range(len(image)):
            if image[i][col] == "1":
                return True
        return False 
