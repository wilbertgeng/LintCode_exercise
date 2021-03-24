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
