"""59. 3Sum Closest
"""
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        # write your code here
        ##
        n = len(numbers)
        if n < 3:
            return None
        numbers.sort()
        ans = numbers[0] + numbers[1] + numbers[n - 1]
        diff = ans - target

        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                sum1 = numbers[i] + numbers[left] + numbers[right]
                if sum1 < target:
                    if abs(sum1 - target) < abs(diff):
                        diff = sum1 - target
                        ans = sum1
                    left += 1
                else:
                    if abs(sum1 - target) < abs(diff):
                        diff = sum1 - target
                        ans = sum1
                    right -= 1

        return ans 







        #######
        n = len(numbers)
        numbers.sort()
        if n < 3:
            return None
        ans = numbers[0] + numbers[1] + numbers[n - 1]
        diff = ans - target
        for i in range(n - 2):
            start = i + 1
            end = n - 1
            while start < end:
                sum3 = numbers[i] + numbers[start] + numbers[end]
                if sum3 < target:
                    start += 1
                    if abs(sum3 - target) < abs(diff):
                        ans = sum3
                        diff = sum3 - target
                        print("Answer1: ", ans)
                else:
                    end -= 1
                    if abs(sum3 - target) < abs(diff):
                        ans = sum3
                        diff = sum3 - target

        return ans
