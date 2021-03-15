"""
65. Median of two Sorted Arrays"""
class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findMedianSortedArrays(self, A, B):
        # write your code here
        """算法流程
        令指针p1和p2分别指向两个数组，初始指向位置0。我们需要遍历(m + n)/2 + 1次，
        每次比较两个位置的元素，在第k次比较时，较小的那个值就是两个数组中第k + 1小的数。
        如果一个指针已经走到了数组末尾，那么移动另一个指针，否则每次将指向较小数的指针后移，直到遍历到中位数。
为了将奇偶情况合并，在代码中用了left和right保存中间值，如果是奇数直接返回right，
如果是偶数就返回(left + right) / 2。
时间复杂度：O(m + n)  m和n分别是两个数组的长度。双指针遍历两个数组，指针移动次数是0(m+n)级。
空间复杂度："""
        m = len(A)
        n = len(B)
        left = -1
        right = -1
        p1 = 0
        p2 = 0

        for i in range((m + n) // 2 + 1):
            left = right
            if p1 >= m or p2 < n and A[p1] > B[p2]:
                right = B[p2]
                p2 += 1
            else:
                right = A[p1]
                p1 += 1

        if (m + n) % 2 == 1:
            return right
        return (left + right) / 2
