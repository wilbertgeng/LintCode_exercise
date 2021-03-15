"""382. Triangle Count
"""
class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here\
        S.sort()
        cnt = 0

        for i in range(len(S)):
            left = 0
            right = i - 1
            while left < right:
                if S[left] + S[right] > S[i]:
                    cnt += right - left
                    # print(cnt)
                    right -= 1
                else:
                    left += 1

        return cnt

s = Solution()

res = s.triangleCount([4, 4, 4, 4])
print(res)
